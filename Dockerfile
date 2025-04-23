# Using the official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Command to run the app
CMD /bin/sh -c 'echo "Running on: http://0.0.0.0:8000" && uvicorn app.main:app --host 0.0.0.0 --port 8000'
