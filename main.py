# Import necessary modules and classes from FastAPI and Pydantic
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional,Dict

# Create an instance of the FastAPI class
app = FastAPI()

# In-memory "database" to store user data
users_db = {}


# Models
#  Pydantic model for the User data
class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None


class UserResponse(User):
    user_id: int

# Endpoint to create a new user
@app.post("/users", response_model=UserResponse)
def create_user(user: User):
    print(user)  # Debugging line to check input
    user_id = len(users_db) + 1
    users_db[user_id] = user
    return {**user.dict(), "user_id": user_id}


# Endpoint to retrieve a list of users
@app.get("/users", response_model=List[User])
def get_users(page: int = Query(1, ge=1), limit: int = Query(10, le=100), search: Optional[str] = None):
    start = (page - 1) * limit
    end = start + limit
    filtered_users = [user for user in users_db.values()]
    
    if search:
        filtered_users = [user for user in filtered_users if search.lower() in user.name.lower()]

    return filtered_users[start:end]


# Endpoint to update an existing user by ID
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return {**user.dict(), "user_id": user_id}


# Endpoint to delete a user by ID
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"detail": "User deleted"}

