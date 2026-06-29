from abc import ABC, abstractmethod


class RateLimitStrategy(ABC):
    @abstractmethod
    def allow(self) -> bool:
        pass
