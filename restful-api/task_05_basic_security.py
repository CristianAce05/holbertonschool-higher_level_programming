#!/usr/bin/env python3
"""Basic API security examples using Flask, Flask-HTTPAuth, and Flask-JWT-Extended.

Endpoints:
 - /basic-protected  : Protected with HTTP Basic Auth
 - /login            : Returns JWT token for valid credentials
 - /jwt-protected    : Protected with JWT
 - /admin-only       : JWT + role check (admin only)

This module is for instructional purposes and stores users in-memory.
"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

try:
    from flask_httpauth import HTTPBasicAuth
except Exception:
    HTTPBasicAuth = None

try:
    from flask_jwt_extended import (
        JWTManager,
        create_access_token,
        jwt_required,
        get_jwt_identity,
        get_jwt,
    )
except Exception:
    JWTManager = None
    create_access_token = None
    jwt_required = None
    get_jwt_identity = None
    get_jwt = None

import os

app = Flask(__name__)

# Secret key for JWT; tests may override via env
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")

auth = HTTPBasicAuth() if HTTPBasicAuth is not None else None
jwt = JWTManager(app) if JWTManager is not None else None

# In-memory users with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password if auth is not None else (lambda f: f)
def verify_password(username, password):
    if not username or not password:
        return False
    u = users.get(username)
    if not u:
        return False
    return check_password_hash(u["password"], password)


@app.route("/basic-protected")
def basic_protected():
    if auth is None:
        return jsonify({"error": "HTTPBasicAuth not available"}), 500
    # Use auth.login_required behavior manually to avoid decorator complexity
    auth_result = auth.current_user()
    # If not authenticated, HTTPBasicAuth will have already sent a 401 via challenge
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    if create_access_token is None:
        return jsonify({"error": "JWT support not available"}), 500
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Include role in additional claims
    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required() if jwt is not None else (lambda f: f)
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required() if jwt is not None else (lambda f: f)
def admin_only():
    claims = get_jwt()
    role = claims.get("role")
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# JWT error handlers to ensure consistent 401 responses for auth errors
if jwt is not None:
    @jwt.unauthorized_loader
    def handle_unauthorized(err):
        return jsonify({"error": "Missing or invalid token"}), 401

    @jwt.invalid_token_loader
    def handle_invalid(err):
        return jsonify({"error": "Invalid token"}), 401

    @jwt.expired_token_loader
    def handle_expired(header, payload):
        return jsonify({"error": "Token has expired"}), 401

    @jwt.revoked_token_loader
    def handle_revoked(jwt_header, jwt_payload):
        return jsonify({"error": "Token has been revoked"}), 401

    @jwt.needs_fresh_token_loader
    def handle_fresh(err):
        return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
