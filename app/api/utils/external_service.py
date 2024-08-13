import random
import asyncio


class ExternalService:
    @staticmethod
    async def simulate_request() -> bool:
        await asyncio.sleep(random.uniform(1, 60))
        return random.choice([True, False])
