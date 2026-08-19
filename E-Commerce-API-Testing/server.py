import os
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
cart_db = []
DATABASE_PATH = os.getenv("DATABASE_PATH", "tests/ecommerce.db")


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request: Missing request payload payload"}), 400

    username = data.get("username")
    password = data.get("password")

    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE username = ?", (username,))
        user_record = cursor.fetchone()
    except sqlite3.OperationalError as error:
        app.logger.error(
            f"Database lookup failure occurred on path '{DATABASE_PATH}': {error}")
        return jsonify({"error": f"Internal Server Configuration Bug: {error}"}), 500
    finally:
        if 'conn' in locals():
            conn.close()

    if user_record and user_record[0] == password:
        return jsonify({"token": "secret_bearer_token_xyz"}), 200
    else:
        return jsonify({"error": "invalid credentials"}), 401


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    products_db = {
        "products": [
            {"id": 101, "name": "Laptop", "price": 999},
            {"id": 102, "name": "Phone", "price": 499}
        ]
    }

    auth_header = request.headers.get("Authorization")
    if auth_header != "Bearer secret_bearer_token_xyz":
        return jsonify({"error": "Unauthorized Access"}), 401

    search_query = request.args.get("search")

    if search_query:
        filtered_list = [p for p in products_db["products"]
                         if search_query.lower() in p["name"].lower()]
        return jsonify({"products": filtered_list}), 200

    return jsonify(products_db), 200


@app.route('/api/v1/cart', methods=['POST'])
def add_to_cart():
    auth_header = request.headers.get("Authorization")
    if auth_header != "Bearer secret_bearer_token_xyz":
        return jsonify({"error": "Unauthorized Access"}), 401

    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request: Missing request data context"}), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not product_id or not quantity:
        return jsonify({"error": "Bad Request: Missing parameters"}), 400

    cart_item = {"product_id": product_id, "quantity": quantity}
    cart_db.append(cart_item)

    return jsonify({"status": "success", "message": "Product appended to cart successfully"}), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
