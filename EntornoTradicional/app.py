from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import requests

app = Flask(__name__)

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    username = request.args.get('username')
    password1 = request.args.get('password1')
    password2 = request.args.get('password2')
    email = request.args.get('email')
    if password1 == password2:
        return jsonify({"message":"Sign Up Successful"}), 200 
    else:
        return jsonify({"error":"Sign Up NOT Successful"}), 400  

@app.route('/api/auth/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    user = "user" ## Consulta a base de datos
    if user:
        token = create_access_token(identity=user)
        return jsonify({"message":"Sign Up Successful", "token":token}), 200 
    else:
        return jsonify({"error":"Sign Up NOT Successful"}), 400 

@app.route('/api/tasks')
def task():
    return "Log In"

if __name__ == '__main__':
    app.run(port=8000)