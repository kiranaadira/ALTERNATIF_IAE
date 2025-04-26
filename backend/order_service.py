from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy data for orders
orders = [
    {"order_id": 1, "user_id": 1, "event_id": 1, "quantity": 2, "total": 200.00, "order_date": "2025-04-26"},
    {"order_id": 2, "user_id": 2, "event_id": 2, "quantity": 1, "total": 50.00, "order_date": "2025-04-26"},
    {"order_id": 3, "user_id": 3, "event_id": 3, "quantity": 3, "total": 225.00, "order_date": "2025-04-26"}
]

# Endpoint untuk mendapatkan daftar order dengan data user dan event yang terhubung
@app.route('/orders', methods=['GET'])
def get_orders():
    result = []
    
    for order in orders:
        try:
            # Mengambil data pengguna dari user_service.py
            user_response = requests.get(f'http://127.0.0.1:5000/users/{order["user_id"]}')
            # Mengambil data event dari event_service.py
            event_response = requests.get(f'http://127.0.0.1:5001/events/{order["event_id"]}')
            
            # Cek jika kedua respons berhasil
            if user_response.status_code == 200 and event_response.status_code == 200:
                user = user_response.json()
                event = event_response.json()

                # Menggabungkan data order dengan nama user dan nama event
                order_details = {
                    "order_id": order["order_id"],
                    "user_id": order["user_id"],
                    "user_name": user["name"],  # Nama user dari response user_service
                    "event_id": order["event_id"],
                    "event_name": event["name"],  # Nama event dari response event_service
                    "quantity": order["quantity"],
                    "total": order["total"],
                    "order_date": order["order_date"]
                }
                result.append(order_details)
            else:
                # Jika salah satu service gagal, beri pesan error yang sesuai
                result.append({
                    "order_id": order["order_id"],
                    "error": "Failed to retrieve user or event data."
                })
        except Exception as e:
            result.append({
                "order_id": order["order_id"],
                "error": f"Error occurred: {str(e)}"
            })

    return jsonify(result)

# Endpoint untuk membuat order baru
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_data = request.json
        user_id = order_data.get('user_id')  # Ambil user_id dari request body
        event_id = order_data.get('event_id')  # Ambil event_id dari request body
        quantity = order_data.get('quantity', 1)  # Default quantity to 1 if not provided
        total = order_data.get('total', 0)  # Default total to 0 if not provided

        # Debug log untuk mengecek data yang diterima
        print(f"Received data: user_id = {user_id}, event_id = {event_id}, quantity = {quantity}, total = {total}")
        
        # Validasi input
        if not isinstance(user_id, int) or not isinstance(event_id, int):
            return jsonify({"message": "Invalid user_id or event_id"}), 400
        
        # Pastikan user_id dan event_id valid
        user_response = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
        event_response = requests.get(f'http://127.0.0.1:5001/events/{event_id}')
        
        if user_response.status_code != 200 or event_response.status_code != 200:
            return jsonify({"message": "Invalid user or event"}), 400

        # Create a new order
        order_id = len(orders) + 1  # Generating new order ID
        new_order = {
            "order_id": order_id,
            "user_id": user_id,
            "event_id": event_id,
            "quantity": quantity,
            "total": total,
            "order_date": "2025-04-26"  # Example order date
        }

        # Log the new order being added
        print(f"Adding new order: {new_order}")

        orders.append(new_order)  # Add the new order to the orders list
        
        # Debug log to check the orders list after adding
        print(f"Updated orders list: {orders}")

        return jsonify({"message": "Order created successfully!", "order_id": order_id}), 201
    except Exception as e:
        print(f"Error creating order: {str(e)}")
        return jsonify({"message": f"Error creating order: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5002)
