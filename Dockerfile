# Use the official Python 3.12 slim image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY text_detection.py backend.py frontend.py requirements.txt .env ./

# Install system dependencies required for Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit default port
EXPOSE 8501

# Set environment variable to ensure Streamlit runs on the correct port
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Command to run the Streamlit application
CMD ["streamlit", "run", "frontend.py"]