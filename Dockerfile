FROM ubuntu:latest
LABEL authors="shan-perera"

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into /app
COPY . /app

# Add /app to PYTHONPATH so that Python can find the 'com' package
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "app.py"]
