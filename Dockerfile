FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose GCS UI (8000) and Telemetry Server (8001)
EXPOSE 8000 8001

# Default command: launch both servers
CMD python telemetry_server.py & python app.py
