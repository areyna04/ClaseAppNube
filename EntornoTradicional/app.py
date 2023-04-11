from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/auth/signup')
def signup():
    return "Sign Up"

@app.route('/api/auth/login')
def signup():
    return "Log In"