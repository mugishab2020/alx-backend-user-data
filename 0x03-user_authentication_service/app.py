#!/usr/bin/env python3
'''setting the flask app
'''
from flask import Flask, jsonify, request, abort
from flask import make_response, redirect, url_for
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def bienvenue():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def Register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"error": "email already exists"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not password or not email:
        abort(401)
    if AUTH.valid_login(email=email, password=password) is False:
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
