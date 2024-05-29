#!/usr/bin/env python3
'''setting the flask app
'''
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
