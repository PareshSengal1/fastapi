from fastapi import FastAPI, HTTPException
from markdown_it.rules_block import table

from schemas import UserCreate, UserResponse, ResResponse, ResCreate
import uvicorn
import crud
from models import create_table

app = FastAPI()

create_table()

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    return crud.create_user(user)

@app.get("/users/", response_model=list[UserResponse])
def read_users():
    return crud.get_users()

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate):
    existing_user = crud.get_user(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(user_id, user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    existing_user = crud.get_user(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(user_id)

@app.post("/restaurant/", response_model=ResResponse)
def create_link(link: ResCreate):
    return crud.create_res(link)

if __name__ == '__main__':
    # uvicorn.run(app, host='127.0.0.1', port=8080)
    uvicorn.run(app, host='0.0.0.0', port=8000)
    # uvicorn.run(app, host='172.28.151.117', port=8080)