FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy
WORKDIR /workspace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-m", "pytest", "test_ui_login.py", "-v", "--html=ui_report.html", "--self-contained-html"]
