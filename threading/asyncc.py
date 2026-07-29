import asyncio
import time



async def Fake_api_call():
    await asyncio.sleep(0.02)


async def main(n):
    start = time.time()
    task = [Fake_api_call() for _ in range(n)]
    await asyncio.gather(*task)
    print(f"Async ({n} tasks): {time.time() - start:.2f}s")


asyncio.run(main(1000000))
