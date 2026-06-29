from Ratelimiter.config.config import StrategyType
from Ratelimiter.strategy.fixed_strategy import FixedStrategy
from Ratelimiter.strategy.token_strategy import TokenStrategy


def make_strategy(Strategy_Type, params):
    if Strategy_Type == StrategyType.FIXED:
        return FixedStrategy(**params)
    elif Strategy_Type == StrategyType.TOKEN:
        return TokenStrategy(**params)
    raise ValueError(f"unknown strategy:{Strategy_Type}")
