from Ratelimiter.config.config import CONFIG, StrategyType, Tier
from Ratelimiter.strategy.factory import make_strategy


class RateLimiterService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, Strategy_type=StrategyType.FIXED):
        if hasattr(self, "limiters"):
            return
        self.client_tiers = {"abc": Tier.FREE, "xyz": Tier.PREMIUM}
        self.Strategy_type = Strategy_type
        self.limiters = {}

    def is_allowed(self, api_key):
        tier = self.client_tiers[api_key]

        if api_key not in self.limiters:
            params = CONFIG[self.Strategy_type][tier]
            self.limiters[api_key] = make_strategy(self.Strategy_type, params)
        return self.limiters[api_key].allow()
