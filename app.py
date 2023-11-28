from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
from markupsafe import escape
from flask import request

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27016')
db = client['attendance_flask']

CORS(app)
@app.route('/')
def input():
    result = request.form
    return render_template('result_data.html', result=result)
# def template():
#     return "Server is running"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/passing', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        result = request.form
        # Send result data to result_data HTML file
        return render_template("result_data.html", result=result)
    
    if request.method == 'GET':
        result=[]
        with open('output.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            # print(line.strip()) 
            result.append(line.strip())
        # result = find_target_face()
        return jsonify(result)
        # return render_template("result_data.html", result=result)
 
  
if __name__ == '__main__':
    app.debug=True 
    app.run()