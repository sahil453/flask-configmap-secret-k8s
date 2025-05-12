import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.getenv('APP_NAME', 'Default App')
    return jsonify(message=f"Welcome to {app_name}")

@app.route('/credentials')
def credentials():
    username = os.getenv('APP_USER')
    password = os.getenv('APP_PASS')
    return jsonify(username=username, password=password)

@app.route('/health')
def health():
    return jsonify(status="UP")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
