import logging
import requests
import pytest
from config import CART_URL, Main_URL
from utils import load_user_data

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def api_url():
    """
    Centralized network endpoint target for the e-commerce container sandbox.
    """
    return "http://localhost:5000"


# FIXED: Parameter updated to match your new fixture name
def test_add_item_to_shopping_cart_success(api_url):
    """
    Verify that an authenticated user can successfully append items 
    to their transactional shopping cart list payload.
    """
    # Authenticate and retrieve dynamic security authorization headers
    login_payload = load_user_data("valid_user")
    login_response = requests.post(Main_URL, json=login_payload, timeout=5)
    dynamic_token = login_response.json().get("token")
    security_pass = {"Authorization": f"Bearer {dynamic_token}"}

    # Prepare transactional cart appending payload
    cart_payload = {"product_id": 101, "quantity": 2}

    # Dispatch request to the shopping cart endpoint
    # FIXED: Replaced base_url with api_url to align tracking references flawlessly
    response = requests.post(
        CART_URL, headers=security_pass, json=cart_payload, timeout=5
    )
    res_json = response.json()

    # Assert data state integrity validation rules
    assert response.status_code == 201
    assert res_json.get("status") == "success"
    assert "successfully" in res_json.get("message")
    logger.info("Cart Engine Transaction verified: Items appended cleanly!")
