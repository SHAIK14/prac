import threading
import time


class Store:
    _instance = None

    def __new__(cls, *args, **kwrgs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "data"):
            return
        self.data = {}
        self.expiry = {}
        self.lock = threading.Lock()  # created BEFORE the sweeper starts
        threading.Thread(target=self._sweep, daemon=True).start()

    def set(self, key, val):
        with self.lock:
            self.data[key] = val

    def get(self, key):
        with self.lock:
            if key in self.expiry and time.time() >= self.expiry[key]:
                del self.expiry[key]
                del self.data[key]
                return None
            if key in self.data:
                return self.data[key]
            else:
                return None

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                return True
            return False

    def set_expire(self, key, exp):
        with self.lock:
            self.expiry[key] = time.time() + exp

    def check_expire(self, key):
        # no lock here — only called from inside _sweep, which already holds the lock
        if time.time() >= self.expiry[key]:
            return True
        return False

    def _sweep(self):
        while True:
            time.sleep(1)  # OUTSIDE the lock — never hold the lock while sleeping
            with self.lock:
                for key, val in list(self.expiry.items()):
                    if self.check_expire(key):
                        del self.expiry[key]
                        del self.data[key]
