AI Text Detection Tool

Overview

The AI Text Detection Tool is a production-ready web application designed to analyze text and determine whether it is AI-generated or human-written. Built with Python, Streamlit, and OpenAI's API, the application features a user-friendly interface with a sidebar file uploader, robust data validation using Pydantic, and secure API key management with a .env file. The project is containerized using Docker for consistent deployment across environments.

Features

Text Analysis: Utilizes OpenAI's GPT-4 model to detect if text is AI-generated, providing a confidence score.
Streamlit Frontend: Offers an intuitive web interface with a sidebar for uploading .txt files.
Pydantic Validation: Ensures type safety and input/output validation for reliable processing.
Modular Architecture: Separates concerns with distinct files for text detection logic, backend processing, and frontend display.
Docker Support: Includes a Dockerfile for easy containerization and deployment.
Secure Configuration: Manages sensitive data (OpenAI API key) using
