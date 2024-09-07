FROM ubuntu:latest
LABEL authors="shan-perera"

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY com/crypto /app

EXPOSE 5000

CMD ["python", "app.py"]