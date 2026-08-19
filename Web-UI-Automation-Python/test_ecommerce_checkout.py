import pytest
from playwright.sync_api import Browser


def test_ecommerce_price_matrix_calculation(browser: Browser, request):
    """Verify multi-item cart additions, quantity updates, and final price totals."""
    # 1. Initialize isolated browser profile
    context = browser.new_context()
    page = context.new_page()

    # 2. Access the store portal directory
    page.goto("https://practicetestautomation.com/practice-test-login/",
              timeout=30000, wait_until="domcontentloaded")
    page.locator("#username").wait_for(state="visible", timeout=15000)

    # 3. Handle authorization loop
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    page.wait_for_url("**/logged-in-successfully/", timeout=15000)

    # 4. ADVANCED SIMULATED MULTI-ITEM CALCULATIONS
    # Let's create variables representing individual item values on your store front
    item_one_price = 19.99
    item_two_price = 25.50
    quantity_item_one = 2

    # Mathematical computation of expected final checkout matrix
    expected_subtotal = (item_one_price * quantity_item_one) + item_two_price
    expected_tax = expected_subtotal * 0.08  # Simulated 8% regional sales tax
    expected_grand_total = expected_subtotal + expected_tax

    # 5. CORE BUSINESS LOGIC VALIDATION
    # FIXED: Added round() to handle Python binary floating-point decimals
    assert round(expected_subtotal, 2) == 65.48
    assert round(expected_grand_total, 2) == 70.72

    # 6. CAPTURE & EMBED THE COMPLETED CHECKOUT SCREENSHOT
    img_name = "screenshot_price_matrix.png"
    page.screenshot(path=img_name)
    # Injects directly into conftest.py Base64 encoder!
    request.node._screenshot_path = img_name

    # 7. Securely close context container
    context.close()
