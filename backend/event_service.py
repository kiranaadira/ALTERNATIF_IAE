from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy data for events
events = {
    1: {"name": "Concert A", "price": 100, "date": "2025-05-01"},
    2: {"name": "Theater B", "price": 50, "date": "2025-06-15"},
    3: {"name": "Festival C", "price": 75, "date": "2025-07-20"}
}

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = events.get(event_id)
    return jsonify(event) if event else ('Event not found', 404)

@app.route('/events', methods=['POST'])
def add_event():
    event_data = request.json
    event_id = len(events) + 1
    events[event_id] = event_data
    return jsonify({"event_id": event_id}), 201

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    if event_id in events:
        del events[event_id]
        return jsonify({"message": "Event deleted successfully!"}), 200
    return ('Event not found', 404)

if __name__ == '__main__':
    app.run(port=5001)