Module 11 — Calculation Model with SQLAlchemy, Pydantic, Factory Pattern, and CI/CD

How to run tests locally

# Create & activate venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Postgres (for integration tests)
docker compose up -d db

# Run all tests
pytest


CI/CD section

GitHub Actions runs tests, builds the Docker image, and pushes to Docker Hub on main

Docker Hub link-

https://hub.docker.com/repository/docker/yugpatil/module11_is601