from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.booklog


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/users')
def get_users():
    users = dumps(db.users.find())
    return users


if __name__=="__main__":
    app.run(host='0.0.0.0')