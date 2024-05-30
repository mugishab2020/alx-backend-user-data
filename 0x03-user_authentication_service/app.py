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
    if Auth.valid_login(email=email, password=password) is False:
        abort(401)

    session_id = Auth.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    user = Auth.find_user_by(session_id=session_id)
    if user:
        AUTH.destroy_session(session_id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    session_id = request.cookies.get('session_id', None)
    if session_id is None:
        abort(403)
    user = Auth.get_user_from_session_id(session_id=session_id)
    if user and session_id:
        return jsonify({"email": {{user.email}}}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    email = request.form.get('email')
    try:
        reset = Auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
