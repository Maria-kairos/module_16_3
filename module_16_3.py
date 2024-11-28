from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def use() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    return f"User {user_id} has been deleted"