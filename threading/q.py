import threading
import queue
import time


q = queue.Queue()



def producerPrice():
    for price in [11,222,4,4,33]:
        print(f"price:{price}")
        q.put(price)
        time.sleep(0.5)
    q.put(None)

def producerName():
    for name in ["info", "tcs", "wipro", "rkforge", "suzlon"]:
        print(f"name:{name}")
        q.put(name)
        time.sleep(0.5)
    q.put(None)


def consumer():
    while True :
        val =  q.get()
        if val is None:
            break
        print(f"price and name of the stockL:{val}")

t1 = threading.Thread(target=producerPrice)
t2 = threading.Thread(target=producerName)
t3 = threading.Thread(target=consumer)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("done")
