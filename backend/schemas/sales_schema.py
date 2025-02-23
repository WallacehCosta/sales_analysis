from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    product_name: str
    quantity: int
    price: float
    total_amount: float

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    sale_date: datetime

    class Config:
        orm_mode = True
