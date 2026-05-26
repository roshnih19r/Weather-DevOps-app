# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Requirements copied
COPY requirements.txt .

# Installation of pip
RUN pip install --no-cache-dir -r requirements.txt

# another code copied
COPY . .

# Port exposed
EXPOSE 5000

# App started
CMD ["python", "run.py"]