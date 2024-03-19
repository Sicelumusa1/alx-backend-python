#!/usr/bin/env python3

"""
Loops 10 times, each time asynchronously wait 1 second, then yield a 
random number between 0 and 10
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, each time asynchronously wait 1 second, then yield a 
    random number between 0 and 10
    """
    for _ in range(10):
        #  Asynchronously wait for 1 second
        await asyncio.sleep(1)
        #  Yield a random number between 0 and 10
        yield random.randint(0, 10)
