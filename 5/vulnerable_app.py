import pickle
import subprocess
import os
import sqlite3
import random
import hashlib
from flask import Flask, request, render_template_string, jsonify
import yaml
import json

app = Flask(__name__)

@app.route('/unpickle', methods=['POST'])
def unpickle_data():
    data = request.get_data()
    obj = pickle.loads(data)
    return str(obj)

@app.route('/execute', methods=['GET'])
def execute_command():
    cmd = request.args.get('cmd', 'ls')
    result = subprocess.check_output(cmd, shell=True)
    return result.decode('utf-8')

@app.route('/search', methods=['GET'])
def search_users():
    username = request.args.get('username', '')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return jsonify(cursor.fetchall())

@app.route('/hello', methods=['GET'])
def hello_xss():
    name = request.args.get('name', 'World')

    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)

@app.route('/readfile', methods=['GET'])
def read_file():
    filename = request.args.get('file', 'test.txt')
    with open(filename, 'r') as f:
        return f.read()

@app.route('/yaml-load', methods=['POST'])
def yaml_load():
    data = request.get_data(as_text=True)
    obj = yaml.load(data, Loader=yaml.Loader)
    return str(obj)

DB_PASSWORD = "super_secret_password_123"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def generate_api_key():
    return str(random.randint(1000, 9999))


if __name__ == '__main__':
    app.run(debug=True)

def process_data():
    while True:
        print("Processing...")

def unused_function():
    return "I'm never used"

def calculate_area(width, height):
    return width * height

def calculate_rectangle_area(w, h):
    return w * h

def complicated_function(x, y, z):
    result = 0
    for i in range(10):
        if x > y and y < z or x == y and y != z or x < y and y > z:
            result += i * x * y * z
            if result > 100:
                for j in range(5):
                    result -= j
                    while result < 50:
                        result += 1
    return result
