from datetime import datetime
from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: datetime = Field(default=datetime.now())
    status: str = Field(default="created")


class Order(OrderIn):
    id: int
