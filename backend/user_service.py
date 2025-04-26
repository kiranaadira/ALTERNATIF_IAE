from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy data for users
users = {
    1: {"name": "Alice Smith", "email": "alice@gmail.com"},
    2: {"name": "Bob Johnson", "email": "bob@gmail.com"},
    3: {"name": "Charlie Brown", "email": "charlie@gmail.com"}
}

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    return jsonify(user) if user else ('User  not found', 404)

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user_id = len(users) + 1
    users[user_id] = user_data
    return jsonify({"user_id": user_id}), 201

if __name__ == '__main__':
    app.run(port=5000)