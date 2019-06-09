from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector
import os
import json

app = Flask(__name__)
api = Api(app)


@app.route('/company/violation_count/<string:company_name>')
def get(company_name):
    db = mysql.connector.connect(
        host="easyethics.ccecgtqyo5kq.us-east-1.rds.amazonaws.com",
        user=os.environ['DB_USERNAME'],
        passwd=os.environ['DB_PASSWORD'],
        database="easyethics"
    )
    cursor = db.cursor()

    company_name = company_name.upper()

    query = """
    SELECT c.name, r.rating, COUNT(r.rating) as violation_count
    FROM companies c
    JOIN ratings r
    ON c.id = r.company
    WHERE UPPER(c.name) = '{company_name}'
    GROUP BY c.name, r.rating
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

app.run(host='0.0.0.0', port=80)
