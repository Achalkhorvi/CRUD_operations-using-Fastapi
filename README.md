# FastAPI User Management API

This project is a simple FastAPI application that provides endpoints for managing users. It includes functionalities for creating, retrieving, updating, and deleting users. The data is stored in an in-memory database.

# First, create a directory for project 
 my directory name is CRUD

# Create a virtual environment to manage your project's dependencies by using command 
python -m venv env

# Activate the virtual environment:
env\Scripts\activate  (for windows)

# Installing required packages
pip install fastapi uvicorn

## Code Explanation
Import necessary modules and classes from FastAPI and Pydantic
Initializes the FastAPI application with `app = FastAPI()`. 
Uses `users_db = {}` to store user data in memory. 
Defines the `User` class with Pydantic to validate and structure user data. It includes required fields (`name`, `email`) and (`age`).

## CRUD Operations
The `POST /users` endpoint allows adding new users. 
The `GET /users` endpoint retrieves a list of users with support for pagination and optional search. 
The `PUT /users/{user_id}` endpoint updates an existing user's details by their ID. 
The `DELETE /users/{user_id}` endpoint removes a user by their ID. 

## Runn the Application
uvicorn main:app --reload

## Access the API documentation:
Open your web browser and navigate to http://127.0.0.1:8000/docs to view and interact with the interactive API documentation provided by FastAPI.





