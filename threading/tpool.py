
from concurrent.futures import ThreadPoolExecutor
import time


def task():
    time.sleep(0.1)

start = time.time()


with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(lambda _:task() , range(1000))

print(f"With pool (20 workers): {time.time() - start:.2f}s")
