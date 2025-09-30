import secrets
import subprocess
import os
import sqlite3
from flask import Flask, request, render_template, escape, jsonify
import yaml
import bcrypt
from pathlib import Path

app = Flask(__name__)

@app.route('/unpickle', methods=['POST'])
def unpickle_data():
    data = request.get_json()
    return jsonify({"status": "Use JSON for serialization"})

@app.route('/execute', methods=['GET'])
def execute_command():
    allowed_commands = {'ls': ['ls', '-la'], 'pwd': ['pwd']}
    cmd = request.args.get('cmd', 'ls')
    if cmd in allowed_commands:
        result = subprocess.run(
            allowed_commands[cmd], 
            capture_output=True, 
            text=True, 
            shell=False
        )
        return result.stdout
    return "Command not allowed"

@app.route('/search', methods=['GET'])
def search_users():
    username = request.args.get('username', '')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return jsonify(cursor.fetchall())

@app.route('/hello', methods=['GET'])
def hello_xss():
    name = request.args.get('name', 'World')
    safe_name = escape(name)
    return f"<h1>Hello, {safe_name}!</h1>"

@app.route('/readfile', methods=['GET'])
def read_file():
    filename = request.args.get('file', 'test.txt')
    base_dir = Path('/safe/directory')
    file_path = (base_dir / filename).resolve()
    if base_dir.resolve() not in file_path.parents:
        return "Access denied", 403
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found", 404

@app.route('/yaml-load', methods=['POST'])
def yaml_load():
    data = request.get_data(as_text=True)
    obj = yaml.safe_load(data)
    return str(obj)

DB_PASSWORD = os.environ.get('DB_PASSWORD', 'default_strong_password')
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
def generate_api_key():
    return secrets.token_urlsafe(32)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
def process_data(max_iterations=1000):
    for i in range(max_iterations):
        print("Processing...")
        if i >= max_iterations - 1:
            break
def calculate_area(width, height):
    return width * height
def simplified_function(x, y, z):
    if x > y:
        return min(x * y * z, 100)
    return max(x + y + z, 0)
