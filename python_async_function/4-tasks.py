#!/usr/bin/env python3
"""Execute multiple tasks concurrently and return their delays."""


import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute task_wait_random n times concurrently and return delays."""
    results = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        results.append(delay)

    return results
