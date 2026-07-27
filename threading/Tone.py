import threading
import time

def worker (name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} ending")

start = time.time()

t1 = threading.Thread(target=worker , args =("Thread-1",))
t2 = threading.Thread(target=worker , args =("Thread-2",))

t1.start()
t2.start()

# t1.join()
# t2.join()

print(f"Total time: {time.time() - start:.2f}s")
