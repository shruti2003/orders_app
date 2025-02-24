from pydantic import BaseModel

class Order(BaseModel):
    symbol: str
    quantity: int
    order_type: str
    price: float
