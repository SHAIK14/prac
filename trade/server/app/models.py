from dataclasses import dataclass

@dataclass
class Trade:
    id:int
    symbol:str
    side:str
    price:float
    qty:float
    worker_id:int
    timestamp:float
