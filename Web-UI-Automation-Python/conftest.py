import pytest
import os
import base64


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Global configuration hook fully compatible with pytest-html v4.x tables."""
    outcome = yield
    report = outcome.get_result()

    # We only inject the screenshot during the actual execution phase ('call')
    if report.when == "call":
        screenshot_path = getattr(item, "_screenshot_path", None)

        if screenshot_path and os.path.exists(screenshot_path):
            import pytest_html

            # Convert image to secure text Base64 data string
            with open(screenshot_path, "rb") as image_file:
                encoded_string = base64.b64encode(
                    image_file.read()).decode("utf-8")

            # Build a fully self-contained HTML image tag
            html_image_data = (
                f'<div>'
                f'<p><b>Test Runtime Screenshot Artifact:</b></p>'
                f'<img src="data:image/png;base64,{encoded_string}" '
                f'style="width:400px; max-height:300px; border:2px solid #ccc; cursor:pointer;" '
                f'onclick="window.open(this.src)" />'
                f'</div>'
            )

            # PRO-TIP v4: Correctly append raw HTML elements using the extra property directly
            if not hasattr(report, "extra"):
                report.extra = []
            report.extra.append(pytest_html.extras.html(html_image_data))
