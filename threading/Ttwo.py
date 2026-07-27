import threading
import time


def cpu_task():
    count = 0
    for _ in range(50_000_000):
        count +=1

start = time.time()

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()
t1.join()
t2.join()
print(f"thread: {time.time() - start:.2f}s")

cpu_task()
cpu_task()
print(f"Sequential: {time.time() - start:.2f}s")
