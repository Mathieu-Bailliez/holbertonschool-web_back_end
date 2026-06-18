#!/usr/bin/env python3
"""Module defining an asynchronous random delay coroutine."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
