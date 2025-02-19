#!python
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Simple API!"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

if __name__ == '__main__':
    app.run(host="192.168.1.3", port=8080, debug=True)
