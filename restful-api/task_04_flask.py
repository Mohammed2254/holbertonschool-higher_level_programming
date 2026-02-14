"""first flask thing in my entire life"""

from flask import Flask
from flask import jsonify
from flask import request
import json

users = {}
app = Flask(__name__)


@app.route("/")
def home():
    """main"""
    return "Welcome to the Flask API!"


@app.route("/data")
def res():
    """"""
    return jsonify(list(users.keys()))


@app.route("/status")
def sta():
    """"""

    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    dictForUser = request.get_json(silent=True)

    if not dictForUser or not isinstance(dictForUser, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in dictForUser:
        return jsonify({"error": "Username is required"}), 400

    username = dictForUser["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = dictForUser

    return jsonify({"message": "User added", "user": dictForUser}), 201

if __name__ == "__main__":
    app.run("localhost", port=5000)
