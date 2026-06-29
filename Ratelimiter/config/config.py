from enum import Enum


class Tier(Enum):
    FREE = "free"
    PREMIUM = "Premium"


class StrategyType(Enum):
    TOKEN = "token_bucket"
    FIXED = "fixed_window"


CONFIG = {
    StrategyType.TOKEN: {
        Tier.FREE: {
            "capacity": 5,
            "refill_rate": 1,
        },
        Tier.PREMIUM: {
            "capacity": 100,
            "refill_rate": 10,
        },
    },
    StrategyType.FIXED: {
        Tier.FREE: {
            "limit": 5,
            "window_size": 10,
        },
        Tier.PREMIUM: {
            "limit": 100,
            "window_size": 10,
        },
    },
}
