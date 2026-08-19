import logging
import requests
import pytest
from utils import load_user_data
from config import Main_URL

logger = logging.getLogger(__name__)


@pytest.fixture
def api_url():
    """Provides the authentication endpoint configuration."""
    return Main_URL


def test_login_success(api_url):
    """
    Verify successful user authentication using dynamic JSON credentials.
    """
    payload = load_user_data("valid_user")
    logger.info("sending Dynamic POST request payload for username: %s",
                payload.get("username"))
    response_post = requests.post(api_url, json=payload, timeout=5)
    res_json = response_post.json()
    assert response_post.status_code == 200
    assert res_json.get("token") == "secret_bearer_token_xyz"
    logger.info("Athentication verified! Token intercepted successfully. ")
