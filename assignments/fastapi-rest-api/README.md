# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create and run a simple RESTful web service using the FastAPI framework. Students will define routes, use Pydantic models for request/response validation, and test endpoints locally.

## 📝 Tasks

### 🛠️	Set up a FastAPI project

#### Description
Initialize a new Python project, install FastAPI and Uvicorn, and create a basic `main.py` file with an application instance.

#### Requirements
Completed program should:

- Have a Python virtual environment (optional, but recommended)
- Install `fastapi` and `uvicorn` via pip
- Contain a `main.py` with a FastAPI app instance
- Include a root endpoint (`/`) returning a welcome message

### 🛠️	Define and use Pydantic models

#### Description
Add endpoints that accept and return data structured by Pydantic models to demonstrate validation and automatic documentation.

#### Requirements
Completed program should:

- Define at least one Pydantic model (e.g. `Item` with fields `name`, `price`, and `is_offer`)
- Implement a POST endpoint `/items/` that accepts the model and returns it in the response
- Implement a GET endpoint `/items/{item_id}` that returns a sample item

### 🛠️	Run and test the API

#### Description
Start the server with Uvicorn and verify the endpoints work by sending requests (curl, httpie, or browser).

#### Requirements
Completed program should:

- Run the server using `uvicorn main:app --reload`
- Use the interactive Swagger UI at `/docs` or ReDoc at `/redoc` to test endpoints
- Demonstrate at least one successful POST and GET request in documentation or comments