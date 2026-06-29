import time

from Ratelimiter.strategy.ratelimiting_strategy import RateLimitStrategy


class TokenStrategy(RateLimitStrategy):
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()

    def allow(self) -> bool:
        pass
