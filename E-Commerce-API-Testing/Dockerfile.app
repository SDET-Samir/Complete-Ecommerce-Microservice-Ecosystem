FROM python:3.11-slim

WORKDIR /workspace

COPY requirements.txt .

RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "server.py"]
