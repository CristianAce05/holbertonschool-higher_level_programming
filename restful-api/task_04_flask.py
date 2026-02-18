#!/usr/bin/env python3
"""Simple Flask API for teaching purposes.

Endpoints:
 - /           : Welcome text
 - /data       : JSON list of usernames
 - /status     : Plain text OK
 - /users/<username> : Return user object or 404
 - /add_user   : POST to add a user

Note: `users` is an in-memory dict and starts empty to avoid shipping test data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users store (username -> user dict). Start empty per instructions.
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
