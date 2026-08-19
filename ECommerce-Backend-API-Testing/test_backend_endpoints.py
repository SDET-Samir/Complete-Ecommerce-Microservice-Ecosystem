import pytest
import requests

# Local server endpoint path definition
LOCAL_API_URL = "http://127.0.0.1:5000"


def test_local_backend_user_fetch():
    """Verify that our local server database securely fetches user profiles."""
    target_endpoint = f"{LOCAL_API_URL}/api/users/2"

    response = requests.get(target_endpoint, timeout=6)

    # Assertions
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["data"]["id"] == 2
    assert response_json["data"]["first_name"] == "Janet"
    assert response_json["data"]["last_name"] == "Weaver"


def test_local_backend_checkout_matrix_calculation():
    """Verify that our backend API accurately computes a multi-item checkout order."""
    target_endpoint = f"{LOCAL_API_URL}/api/checkout"

    # Simulating a payload packet containing product info
    payload_data = {
        "item_price": 19.99,
        "quantity": 2
    }

    # Fire a POST request containing our data packet
    response = requests.post(target_endpoint, json=payload_data, timeout=6)

    assert response.status_code == 200
    response_json = response.json()

    # Assert backend calculations math matches perfectly
    assert response_json["status"] == "success"
    assert response_json["calculations"]["subtotal"] == 39.98
    assert response_json["calculations"]["tax"] == 3.20  # 39.98 * 0.08 rounded
    assert response_json["calculations"]["grand_total"] == 43.18
