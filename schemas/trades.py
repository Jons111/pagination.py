from pydantic import BaseModel
from typing import Optional

class TradeBase(BaseModel):
    product_id:int
    order_id:int
    name: str
    last_name: Optional[str] = None
    address: str
    number: str



class TradeCreate(TradeBase):
    pass

class TradeUpdate(TradeBase):
    id:int
    status:bool