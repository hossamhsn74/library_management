# Library Management System

This project implements a library management system focusing on CRUD operations for borrowing books. It includes models for books and borrow records, and provides API endpoints for managing these entities.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Running the App](#running-the-app)
- [Testing](#testing)
- [Docker](#docker)
- [API Documentation](#api-documentation)
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

### Installation

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

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Running the App

1. Ensure the virtual environment is activated.
2. Start the Django development server:
    ```bash
    python manage.py runserver
    ```
3. Open a browser and navigate to `http://127.0.0.1:8000/` to see the application running.

## Testing

### Running Unit Tests

1. Ensure the virtual environment is activated.
2. Run the tests using pytest:
    ```bash
    pytest
    ```

### Loading Dummy Data

1. Load initial data from the fixture file:
    ```bash
    python manage.py loaddata initial_data.json
    ```

## Docker

### Docker Configuration

1. Build the Docker image:
    ```bash
    docker-compose build
    ```

2. Start the containers:
    ```bash
    docker-compose up
    ```

3. Apply migrations and create a superuser inside the web container:
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

4. The application will be available at `http://127.0.0.1:8000/`.

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
Each book can only be borrowed by one user at a time.
Borrow records are updated to mark books as returned.
Authentication is required for all operations.