from fastapi import FastAPI
import uvicorn
from db import database
from routers.orders import router as router_orders
from routers.products import router as router_products
from routers.users import router as router_users


app = FastAPI()
app.include_router(router_orders, tags=["orders"])
app.include_router(router_products, tags=["products"])
app.include_router(router_users, tags=["users"])


@app.get("/")
def root():
    return 'Welcome!'


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True
    )
