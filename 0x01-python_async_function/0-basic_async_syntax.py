#!/usr/bin/env python3

"""
Defines a basic asynchronous coroutine
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay(10)
    Args:
        int: maximum delay
    Returns:
        float: random delay 
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
