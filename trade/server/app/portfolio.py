import threading
from app.models import Trade


class Portfolio:
    def __init__(self):
        self._holdings ={}
        self.lock =  threading.Lock()

    def apply_trade(self , trade : Trade):
        with self.lock:
            change = trade.qty if trade.side == "BUY" else -trade.qty
            self._holdings[trade.symbol] = self._holdings.get(trade.symbol , 0) + change

    def get_holdings (self):
        with self.lock:
            return dict(self._holdings)
