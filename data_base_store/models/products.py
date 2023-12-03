from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: int = Field(default=0)


class Product(ProductIn):
    id: int
