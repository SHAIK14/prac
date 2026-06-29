import time

from Ratelimiter.strategy.ratelimiting_strategy import RateLimitStrategy


class FixedStrategy(RateLimitStrategy):
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.count = 0
        self.window_start = time.time()

    def allow(self) -> bool:
        now = time.time()

        if now - self.window_start >= self.window_size:
            self.count = 0
            self.window_start = now
        if self.count <= self.limit:
            self.count += 1
            return True
        return False
