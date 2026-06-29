import time

from cache.store.store import Store

store = Store()

# 1. basic set / get
store.set("name", "asif")
print("get name      ->", store.get("name"))  # asif

# 2. delete
store.delete("name")
print("get after del ->", store.get("name"))  # None

# 3. TTL: set a key that expires in 2 seconds
store.set("session", "abc123")
store.set_expire("session", 2)
print("get session   ->", store.get("session"))

print("sleeping 3s... (past the 2s TTL)")
time.sleep(3)
print("get session   ->", store.get("session"))
