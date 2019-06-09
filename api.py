from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import mysql.connector
import os
import json

app = Flask(__name__)
api = Api(app)


@app.route('/violation_count')
def violation_count():
    db = mysql.connector.connect(
        host="easyethics.ccecgtqyo5kq.us-east-1.rds.amazonaws.com",
        user=os.environ['DB_USERNAME'],
        passwd=os.environ['DB_PASSWORD'],
        database="easyethics"
    )
    cursor = db.cursor()

    company_name = request.args.get('company_name', type=str).upper()

    query = """
    SELECT c.name, r.rating, COUNT(r.rating) as violation_count
    FROM companies c
    JOIN ratings r
    ON c.id = r.company
    WHERE UPPER(c.name) = '{company_name}'
    GROUP BY c.name, r.rating;
    """.format(
        company_name=company_name
    )

    cursor.execute(query)

    result = cursor.fetchall()

    api_result = {
        'company': {
            'name': result[0][0],
            'violations': []
        }
    }

    for r in result:
        print(r)
        api_result['company']['violations'].append({
            'violation_name': r[1],
            'violation_count': r[2]
        })

    json_result = json.dumps(api_result, sort_keys=True)
    return json_result, 200


@app.route('/banned_company')
def banned_company():
    db = mysql.connector.connect(
        host="easyethics.ccecgtqyo5kq.us-east-1.rds.amazonaws.com",
        user=os.environ['DB_USERNAME'],
        passwd=os.environ['DB_PASSWORD'],
        database="easyethics"
    )
    cursor = db.cursor()

    user_id = request.args.get('user_id', type=int)
    company_name = request.args.get('company_name', type=str).upper()

    query = """
    SELECT
        *
    FROM
        ratings r
    JOIN companies c
    ON r.company = c.id
    WHERE
        r.user = {user_id} AND UPPER(c.name) = '{company_name}';
    """.format(
        user_id=user_id,
        company_name=company_name
    )

    cursor.execute(query)

    result = cursor.fetchall()
    print(result)
    if len(result) > 0:
        return 'True', 200
    else:
        return 'False', 200


app.run(host='0.0.0.0', port=80)
