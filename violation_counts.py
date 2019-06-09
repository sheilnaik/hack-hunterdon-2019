from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import mysql.connector
import os
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'
api = Api(app)


class Company(Resource):
    def get(self, company):
        db = mysql.connector.connect(
            host="easyethics.ccecgtqyo5kq.us-east-1.rds.amazonaws.com",
            user=os.environ['DB_USERNAME'],
            passwd=os.environ['DB_PASSWORD'],
            database="easyethics"
        )
        cursor = db.cursor()

        company = company.upper()

        query = """
        SELECT c.name, r.rating, COUNT(r.rating) as violation_count
        FROM companies c
        JOIN ratings r
        ON c.id = r.company
        WHERE UPPER(c.name) = '{company_name}'
        GROUP BY c.name, r.rating
        """.format(
            company_name=company
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

        json_result = json.dumps(api_result)
        return json_result, 200

api.add_resource(Company, "/company/<string:company>")

app.run(host='0.0.0.0', port=80)
