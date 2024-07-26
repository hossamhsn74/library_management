# Library Management System

This project implements a library management system focusing on CRUD operations for borrowing books. It includes models for books and borrow records, and provides API endpoints for managing these entities.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Running the App (using Virtualenv)](#running-the-app-with-virtualenv)
- [Runnung the App (using Docker)](#running-the-app-with-docker)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [Example Endpoints](#example-endpoints)
- [Assumptions](#assumptions)

## Features

- CRUD operations for books
- CRUD operations for borrow records
- Borrowing and returning books
- Authentication and authorization using JWT
- Comprehensive API documentation

## Setup

### Prerequisites

- Python 3.8+
- Django 3.2+
- Docker (if using Docker setup)

### Installation (using Virtualenv)

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. rename `env-template` file to `.env`.

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Navigate to `settings.py` and uncomment the first block for db connections where `sqlite3` is used.

6. Apply migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

8. Load initial data:
    ```bash
    python manage.py loaddata initial_data.json
    ```

9. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Running the App With Virtualenv

1. Ensure the virtual environment is activated.
2. Start the Django development server:
    ```bash
    python manage.py runserver
    ```
3. Open a browser and navigate to `http://127.0.0.1:8000/` to see the application running.


## Running the App With Docker
1. rename `env-template` file to `.env`.

2. Navigate to `settings.py` and uncomment the 2nd block for db connections where `postgresql` is being used.

3. Build & Start the Docker image:
this step included build & start the containers and load inital data
    ```bash
    docker-compose up --build
    ```

4. Open a browser and navigate to http://127.0.0.1:8000/ to see the application running.


## Testing

### Running Unit Tests

1. Ensure the virtual environment is activated if you're using it to run the app OR access shell environment for your docker containers.

2. Run the tests using pytest:
    ```bash
    pytest
    ```

### API Documentation
API documentation is available at /docs/ when the server is running.

## Example Endpoints
- List Books: GET /api/books/
- Create Book: POST /api/books/
- Retrieve Book: GET /api/books/{id}/
- Update Book: PUT /api/books/{id}/
- Delete Book: DELETE /api/books/{id}/
- List Borrow Records: GET /api/borrow-records/
- Create Borrow Record: POST /api/borrow-records/
- Retrieve Borrow Record: GET /api/borrow-records/{id}/
- Update Borrow Record: PUT /api/borrow-records/{id}/
- Delete Borrow Record: DELETE /api/borrow-records/{id}/

## Assumptions
- Each book can only be borrowed by one user at a time.
- Borrow records are updated to mark books as returned.
- Authentication is required for all operations.