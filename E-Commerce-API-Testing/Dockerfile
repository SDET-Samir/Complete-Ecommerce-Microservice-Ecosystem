FROM python:3.11-slim

WORKDIR /app

COPY init_db.py .

RUN python init_db.py

CMD ["tail", "-f", "/dev/null"]
