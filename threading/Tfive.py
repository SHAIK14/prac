import threading
import sys
import time

sys.setswitchinterval(0.0000001)


lock_a = threading.Lock()
lock_b = threading.Lock()



counter = 0

def t1_lock():
    lock_a.acquire()
    print("t1 got lock-a")
    time.sleep(1)
    lock_b.acquire()
    print("t1 got lock-b")
    lock_a.release()
    lock_b.release()
def t2_lock():
    lock_a.acquire()
    print("t2 got lock-a")
    time.sleep(1)
    lock_b.acquire()
    print("t2 got lock-b")
    lock_a.release()
    lock_b.release()









t1 = threading.Thread(target=t1_lock)
t2 = threading.Thread(target=t2_lock)

t1.start()
t2.start()

t1.join()
t2.join()
print(counter)
