import threading
from app.models import Trade
class TradeRepository:
    def __init__(self):
        self._trades =[]
        self.next_id = 0
        self.lock = threading.Lock()

    def add(self, trade :Trade ) -> Trade :
        with self.lock:
            trade.id = self.next_id +1
            self.next_id +=1
            self._trades.append(trade)
        return trade

    def get_all(self) -> list[Trade]:
        with self.lock:
            return self._trades.copy()



    def get_latest(self, x=1) -> list[Trade]:
        with self.lock:

            n =len(self._trades)
            latest = self._trades[(n-x):n]
            return latest
