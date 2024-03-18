#!/usr/bin/env python3

"""
Creates an asyncio.task that wait for a random delay between 0 and specified max_delay
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Any:
    """
    Creates an asyncio.task that wait for a random delay between 0 and    specified max_delay

    Args:
        max_delay (int): maimum delay in seconds
    Returns:
        asyncio.task: A task that respresents the asynchronous operation
    """
    return asyncio.create_task(wait_random(max_delay))
