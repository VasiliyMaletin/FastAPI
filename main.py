import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [
    User(id=0, name='test', email='test@example.com', password='dsgdagdfaf')
]


@app.get('/users/', response_model=list[User])
async def get_users():
    return users


@app.get('/users/{id}', response_model=User)
async def get_user(id: int):
    user = [user for user in users if user.id == id]
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user[0]


@app.post('/users/', response_model=User)
async def create_user(user: User):
    if [u for u in users if u.id == user.id]:
        raise HTTPException(status_code=409, detail="User already exist")
    users.append(user)
    return user


@app.put('/users/{id}', response_model=User)
async def update_user(user: User):
    for ind in range(len(users)):
        if users[ind].id == user.id:
            users[ind] = user
        return users[ind]
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/users/{id}')
async def delete_user(id: int):
    for ind in range(len(users)):
        if users[ind].id == id:
            users.pop(ind)
            return {'message': 'User deleted'}
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    uvicorn.run('task_4:app', host='localhost', port=8000, reload=True)
