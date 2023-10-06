from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name:str
    model:str
    real_price:float
    trade_price:float
    description:str



class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    id:int
    status:bool