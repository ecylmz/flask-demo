# Flask Demo - CI/CD with GitHub Actions and Dokku

This is a simple Flask application demonstrating CI/CD principles using GitHub Actions for continuous integration and deployment to a Dokku server.

## Features

- Simple Flask application that greets users
- Environment variable configuration
- Automated tests
- GitHub Actions workflow for CI/CD
- Automatic deployment to Dokku
- Docker containerization
- Docker Compose support for development

## Setup

### Using Python and uv

1. Clone the repository
2. Create a virtual environment with uv:
   ```
   uv venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```
   uv pip install -r requirements.txt
   ```

### Using Docker

You can also run the application using Docker:

```
docker build -t flask-demo .
docker run -p 3000:3000 -e NAME="Your Name" flask-demo
```

### Using Docker Compose

For development, you can use Docker Compose:

```
docker-compose up
```

This will build the image and start the container with the appropriate environment variables and volume mounts.

## Running the Application

### With Python

To run the application locally:

```
export NAME="Your Name"
python app.py
```

### With Docker

```
docker run -p 3000:3000 -e NAME="Your Name" flask-demo
```

### With Docker Compose

```
docker-compose up
```

The application will be available at http://localhost:3000

## Running Tests

```
python -m pytest
```

## CI/CD Setup

To set up CI/CD with GitHub Actions and Dokku:

1. Create a Dokku app on your server
2. Add the following secrets to your GitHub repository:
   - `DOKKU_REMOTE_URL`: SSH URL to your Dokku app (e.g., `ssh://dokku@example.com:22/appname`)
   - `DOKKU_SSH_PRIVATE_KEY`: SSH private key for deployment

The GitHub Actions workflow will:
1. Run tests on every push and pull request
2. Build and test the Docker image
3. Deploy to Dokku when changes are pushed to the main branch

### Dokku Deployment

Dokku supports both buildpack-based deployment (using the Procfile) and Docker-based deployment (using the Dockerfile). This project includes both methods, but Dokku will prioritize the Dockerfile if found.
