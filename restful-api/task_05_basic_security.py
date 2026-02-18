#!/usr/bin/python3

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "a_very_long_random_secret_key_with_more_than_32_chars!"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return username


@app.route('/basic-protected')
@auth.login_required
def index():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def login():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 401
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return jsonify({"error": "Missing username or password"}), 401
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            access_token = create_access_token(identity=username)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"error": "Invalid credentials"}), 401



@app.route("/jwt-protected")
@jwt_required
def jwt_protected():
    actual_user = get_jwt_identity()
    user_info = users.get(actual_user)
    return jsonify({"message": "JWT Auth: Access Granted"})

if __name__ == '__main__':
    app.run()
