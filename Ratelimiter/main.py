from Ratelimiter.service.ratelimiting_service import RateLimiterService

service = RateLimiterService()

for i in range(10):
    res = service.is_allowed("abc")
    print(f"{i + 1}:{'done' if res else ' X 429'}")
