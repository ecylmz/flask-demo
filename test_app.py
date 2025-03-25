import os
import pytest
from app import app

def test_home():
    # Set the environment variable for testing
    os.environ["NAME"] = "Cezmi"

    # Create a test client
    client = app.test_client()

    # Make a request to the home route
    response = client.get("/")

    # Check if the response matches the expected output
    assert response.data == b"Hello, Cezmi. Welcome to the CI/CD World!1"
