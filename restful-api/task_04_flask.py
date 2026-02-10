"""first flask thing in my entire life"""
from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def res():
    return list(users.keys())

@app.route('/status')
def sta():
    return jsonify({"status": "OK"})

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user")
def add_user(data):
    dictUser = json.load(data)
    users[username] = dictUser
    
if __name__ == "__main__": 
    app.run("localhost",port=5000)