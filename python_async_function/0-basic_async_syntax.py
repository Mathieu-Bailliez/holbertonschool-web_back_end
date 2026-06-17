#!/usr/bin/env python3
"""Module définissant une coroutine d'attente aléatoire asynchrone."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Attend de manière asynchrone un délai aléatoire entre 0 et
    max_delay secondes (inclus), puis retourne ce délai sous forme
    de nombre flottant.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
