from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)


# MongoDB connect
client = MongoClient('mongodb://mongodb:27017/')
db = client.mydatabase # Use your database name
collection = db.user_inputs # User your collection name

mydb = client["yukai_test1"]
mycol = mydb["PT_family"]


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/admin")
def admin_page():
    return "<h1>This is the Admin Page</h1>"

# html & I/O & MongoDB
@app.route('/testIO', methods=['GET', 'POST'])
def test_io():
    if request.method == 'POST':
        try:
            user_input = request.form['user_input']

            # Store the input into MongoDB
            data = {'user_input': user_input}
            result = collection.insert_one(data)

            # return insert ID and show on html
            return render_template('index.html', user_input=user_input)
        except KeyError:
            return "Error: 'user_input' not found in form data", 400
    return render_template('index.html', user_input=None)

# PT_family main page
@app.route('/PT_family', methods=['GET', 'POST'])
def pt_main_page():
    return render_template('pt_main.html')

# test api

## Get for MongoDB
@app.route('/PT_family/api/<name>', methods=['GET'])
def get_item_by_name(name):
    item = mycol.find_one({"name": name}, {'_id': 0})
    if item:
        return jsonify(item)
    return jsonify({"error":"item not found"}), 404

## Get all
@app.route('/PT_family/api', methods=['GET'])
def get_all_item():
    items = list(mycol.find({}, {'_id': 0})) # json not able to show id
    return jsonify(items)

## Add into MongoDB 
@app.route('/PT_family/api', methods=['POST'])
def add_item():
    item = request.json
    mycol.insert_one(item)
    return jsonify({"message": "Item added successfully"}), 201

if __name__ == "__main__":
    app.run(port=3333, host="0.0.0.0")
