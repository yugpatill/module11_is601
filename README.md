# Module 11 — Calculation Model with SQLAlchemy, Pydantic, Factory Pattern, and CI/CD

## How to Run Tests Locally

### 1️⃣ Create & activate virtual environment

    python3 -m venv venv
    source venv/bin/activate

### 2️⃣ Install dependencies

    pip install -r requirements.txt

### 3️⃣ Start Postgres (required for integration tests)

    docker compose up -d db

### 4️⃣ Run all tests

    pytest


## CI/CD Pipeline

This project includes a complete CI/CD pipeline using GitHub Actions.  

## Docker Image on Docker Hub

The Docker image is automatically published here:

https://hub.docker.com/repository/docker/yugpatil/module11_is601
