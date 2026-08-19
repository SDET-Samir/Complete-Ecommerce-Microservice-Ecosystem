import logging
import requests
import pytest
from config import CART_URL, Main_URL
from utils import load_user_data

logger = logging.getLogger(__name__)


@pytest.fixture
def base_url():
    """Provides the shopping cart API endpoint."""
    return CART_URL


def test_add_item_to_shopping_cart_success(base_url):
    """
    Verify that an authenticated user can successfully append items 
    to their transactional shopping cart list payload.
    """
    login_payload = load_user_data("valid_user")
    login_response = requests.post(Main_URL, json=login_payload, timeout=5)
    dynamic_token = login_response.json().get("token")
    security_pass = {"Authorization": f"Bearer {dynamic_token}"}

    cart_payload = {"product_id": 101, "quantity": 2}

    response = requests.post(
        base_url, headers=security_pass, json=cart_payload, timeout=5)
    res_json = response.json()
    assert response.status_code == 201
    assert res_json.get("status") == "success"
    assert "successfully" in res_json.get("message")
    logger.info("Cart Engine Transaction verified: Items appended cleanly!")
