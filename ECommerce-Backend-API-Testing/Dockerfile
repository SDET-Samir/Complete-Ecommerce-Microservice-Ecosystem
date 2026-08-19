# 1. Start from an official, optimized lightweight Python Linux image
FROM python:3.11-slim

# 2. Set the secure operational directory inside the virtual container
WORKDIR /app

# 3. Copy our list of ingredients (requirements.txt) into the container
COPY requirements.txt .

# 4. Execute pip to install flask, requests, and pytest inside the container environment
# 4. Execute pip with explicit timeout safety configurations
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# 5. Copy the rest of our backend code (server.py, test_backend_endpoints.py) into the container
COPY . .

# 6. Open network port 5000 so your host computer can talk to the virtual container
EXPOSE 5000

# 7. Define the default engine command to automatically boot up our Flask API server
CMD ["python", "server.py"]
