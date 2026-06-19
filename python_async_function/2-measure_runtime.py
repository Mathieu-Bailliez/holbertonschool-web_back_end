#!/usr/bin/env python3
"""Measure the runtime of wait_n."""


import time
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n."""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    total_time = end - start

    return total_time / n
