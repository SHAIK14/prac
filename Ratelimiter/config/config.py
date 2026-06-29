from enum import Enum


class Teir(Enum):
    Free = "free"
    Premium = "Premium"


class StrategyType(Enum):
    TOKEN = "token_bucket"
    FIXED = "fixed_window"


CONFIG = {
    StrategyType.TOKEN: {
        Teir.Free: {
            "capacity": 5,
            "refill_rate": 1,
        },
        Teir.Premium: {
            "capacity": 100,
            "refill_rate": 10,
        },
    },
    StrategyType.FIXED: {
        Teir.Free: {
            "limit": 5,
            "window_size": 10,
        },
        Teir.Premium: {
            "limit": 100,
            "window_size": 10,
        },
    },
}
