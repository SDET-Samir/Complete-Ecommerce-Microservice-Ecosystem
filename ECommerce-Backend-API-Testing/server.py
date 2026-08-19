from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock Data Store representing our backend database entries
MOCK_USERS_DB = {
    "2": {"id": 2, "first_name": "Janet", "last_name": "Weaver", "role": "QA_Master"}
}


@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """API Endpoint simulating a user database query."""
    if user_id in MOCK_USERS_DB:
        return jsonify({"data": MOCK_USERS_DB[user_id]}), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/api/checkout", methods=["POST"])
def calculate_checkout():
    """API Endpoint simulating an e-commerce shopping cart calculation matrix."""
    data = request.get_json() or {}
    item_price = data.get("item_price", 0)
    quantity = data.get("quantity", 0)

    subtotal = round(item_price * quantity, 2)
    tax = round(subtotal * 0.08, 2)
    grand_total = round(subtotal + tax, 2)

    return jsonify({
        "status": "success",
        "calculations": {
            "subtotal": subtotal,
            "tax": tax,
            "grand_total": grand_total
        }
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
