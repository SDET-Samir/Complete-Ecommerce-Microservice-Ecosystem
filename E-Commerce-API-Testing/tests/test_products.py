import logging
import requests
import pytest
from config import PRODUCTS_URL, Main_URL
from utils import load_user_data

logger = logging.getLogger(__name__)


@pytest.fixture
def api_url():
    return PRODUCTS_URL


def test_get_products_success(api_url):
    """Verifies access to private catalogs using chained dynamic tokens."""
    login_payload = load_user_data("valid_user")
    login_response = requests.post(Main_URL, json=login_payload, timeout=5)

    dynamic_token = login_response.json().get("token")
    logger.info("Dynamic Token intercepted: %s", dynamic_token)

    security_pass = {"Authorization": f"Bearer {dynamic_token}"}
    response = requests.get(api_url, headers=security_pass, timeout=5)

    assert response.status_code == 200
    assert "products" in response.json()
    logger.info("Access Granted: Product database extracted securely.")


def test_get_products_unauthorized(api_url):
    """Verifies that malicious headers are forcefully blocked."""
    fake_pass = {"Authorization": "Bearer HAKER_TOKEN_123"}
    response = requests.get(api_url, headers=fake_pass, timeout=5)

    assert response.status_code == 401
    assert response.json().get("error") == "Unauthorized Access"
    logger.info(
        "Security Alert: Unauthorized hacker block successfully verified.")


def test_get_products_filtered_by_search_query(api_url):
    """
    Verify that the product endpoint accurately filters search records 
    when custom query parameters are passed in the request string.
    """
    login_payload = load_user_data("valid_user")
    login_response = requests.post(Main_URL, json=login_payload, timeout=5)
    dynamic_token = login_response.json().get("token")
    security_pass = {"Authorization": f"Bearer {dynamic_token}"}

    query_param = {"search": "Laptop"}

    response = requests.get(api_url, headers=security_pass,
                            params=query_param, timeout=5)
    res_json = response.json()

    assert response.status_code == 200
    assert len(res_json["products"]) == 1
    assert res_json["products"][0]["name"] == "Laptop"
    logger.info("Query Parameter Validation passed: Target filtering verified!")
