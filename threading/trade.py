import threading
import time
import random
SYMBOLS = ["TCS", "INFY", "WIPRO", "RELIANCE", "HDFC"]
SIDES = ["BUY", "SELL"]
trades =[]
portfolio ={}

lock = threading.Lock()
set_event = threading.Event()
def worker(worker_id):
    while not set_event.is_set():
        stock = random.choice(SYMBOLS)
        side = random.choice(SIDES)
        qty = random.randint(500,1000)
        trade ={"worker_id": worker_id , "stock": stock ,"side": side,"qty": qty}
        with lock:
            trades.append(trade)
            change = qty if side =="BUY" else -qty
            portfolio[stock] = portfolio.get(stock, 0) + change
            print(f"Worker-{worker_id}: {trade} | Portfolio: {portfolio}")

        time.sleep(1)


threads =[threading.Thread(target =worker , args =(i,))for i in range(3)]

for t in threads:
    t.start()

# time.sleep(5)

set_event.set()

for t in threads:
    t.join()

print("done")
