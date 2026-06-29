import time

from Ratelimiter.strategy.ratelimiting_strategy import RateLimitStrategy


class FixedStrategy(RateLimitStrategy):
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.count = 0
        self.window_start = time.time()

    def allow(self) -> bool:
        pass
