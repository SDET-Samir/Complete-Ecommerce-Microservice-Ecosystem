import pytest
from playwright.sync_api import Browser

# --- TEST CASE 1: ISOLATED POSITIVE LOGIN ---


def test_positive_login(browser: Browser, request):
    """Verify successful login redirects using an isolated context profile."""
    context = browser.new_context()
    page = context.new_page()

    # FIXED: Full URL path restored
    page.goto("https://practicetestautomation.com/practice-test-login/",
              timeout=30000, wait_until="domcontentloaded")
    page.locator("#username").wait_for(state="visible", timeout=15000)

    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

    page.wait_for_url("**/logged-in-successfully/", timeout=15000)

    img_name = "screenshot_success.png"
    page.screenshot(path=img_name)
    request.node._screenshot_path = img_name
    context.close()


# --- TEST CASE 2: NEGATIVE USERNAME ---
def test_negative_username(browser: Browser, request):
    """Verify that an incorrect username triggers an error message."""
    context = browser.new_context()
    page = context.new_page()

    # FIXED: Full URL path restored
    page.goto("https://practicetestautomation.com/practice-test-login/",
              timeout=30000, wait_until="domcontentloaded")
    page.locator("#username").wait_for(state="visible", timeout=15000)

    page.locator("#username").fill("incorrectUser")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

    error_message = page.locator("#error")
    assert "Your username is invalid!" in error_message.inner_text()

    img_name = "screenshot_invalid_username.png"
    page.screenshot(path=img_name)
    request.node._screenshot_path = img_name
    context.close()


# --- TEST CASE 3: NEGATIVE PASSWORD ---
def test_negative_password(browser: Browser, request):
    """Verify that an incorrect password triggers an error message."""
    context = browser.new_context()
    page = context.new_page()

    # FIXED: Full URL path restored
    page.goto("https://practicetestautomation.com/practice-test-login/",
              timeout=30000, wait_until="domcontentloaded")
    page.locator("#username").wait_for(state="visible", timeout=15000)

    page.locator("#username").fill("student")
    page.locator("#password").fill("incorrectPassword")
    page.locator("#submit").click()

    error_message = page.locator("#error")
    assert "Your password is invalid!" in error_message.inner_text()

    img_name = "screenshot_invalid_password.png"
    page.screenshot(path=img_name)
    request.node._screenshot_path = img_name
    context.close()
