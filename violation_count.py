from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector

app = Flask(__name__)

api = Api(app)

def connect_to_db():
    db = mysql.connector.connect(
        host="easyethics.ccecgtqyo5kq.us-east-1.rds.amazonaws.com",
        user="hackhunterdon",
        passwd="hackhunterdon",
        database="easyethics"
    )

    cursor = db.cursor()

    return cursor


class Company(Resource):
    def get(self, company):
        db = mysql.connector.connect(
            host="easyethics.ccecgtqyo5kq.us-east-1.rds.amazonaws.com",
            user="hackhunterdon",
            passwd="hackhunterdon",
            database="easyethics"
        )

        cursor = db.cursor()

        company = company.upper()

        query = "SELECT COUNT(*) FROM easyethics.companies WHERE UPPER(name) LIKE '%{company_name}%'".format(
            company_name=company
        )

        cursor.execute(query)

        myresult = cursor.fetchall()
        name = myresult[0][0]

        cursor.close()
        db.close()

        return name, 200

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(Company, "/company/<string:company>")

app.run(host='0.0.0.0')

