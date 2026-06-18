#!/usr/bin/env python3
"""Execute multiple coroutines concurrently."""


import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times concurrently and return delays."""
    results = []

    coroutines = []

    for _ in range(n):
        coro = wait_random(max_delay)
        coroutines.append(coro)

    for completed in asyncio.as_completed(coroutines):
        delay = await completed
        results.append(delay)

    return results
