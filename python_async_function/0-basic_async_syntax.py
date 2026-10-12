#!/usr/bin/env python3
"""
Module that defines an asynchronous coroutine waiting for a random delay.

A coroutine is a function declared with `async def` that can pause at each
`await` and resume later, letting other coroutines run in the meantime.

Calling a coroutine does not execute it: it only creates a coroutine object,
which must be run with `await` or `asyncio.run()`.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine that waits a random delay between 0 and max_delay and
    returns it."""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
