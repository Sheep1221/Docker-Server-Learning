from flask import Flask
from pymongo import MongoClient
from .api_route import init_api_routes
from .web_route import init_web_routes

def create_app():
    app = Flask(__name__)
    
    # MongoDB connect
    client = MongoClient('mongodb://mongodb:27017/')
    mydb = client["yukai_test1"]
    mycol = mydb["PT_family"]
    app.mycol = mycol

    init_api_routes(app)
    init_web_routes(app)

    return app
