from fastapi import APIRouter, HTTPException
from db import database, orders
from models.orders import OrderIn, Order

router = APIRouter()


@router.post('/orders/')
async def add_order(order: OrderIn):
    query = orders.insert().values(**order.dict())
    await database.execute(query)
    return {'msg': 'Order added'}


@router.get('/orders/', response_model=list[Order])
async def get_orders():
    orders_ = orders.select()
    return await database.fetch_all(orders_)


@router.get('/orders/{id}', response_model=Order)
async def get_order(id: int):
    query = orders.select().where(orders.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Order not found")


@router.put('/orders/{id}', response_model=Order)
async def update_order(id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == id).values(**order.dict())
    result = await database.execute(query)
    if result:
        return {**order.dict(), 'id': id}
    raise HTTPException(status_code=404, detail="Order not found")


@router.delete('/orders/')
async def delete_order(id: int):
    query = orders.delete().where(orders.c.id == id)
    result = await database.execute(query)
    if result:
        return {'msg': 'Order deleted'}
    raise HTTPException(status_code=404, detail="Order not found")
