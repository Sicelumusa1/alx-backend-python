#!/usr/bin/env python3

"""
Spawn wait_random n times with the specified max_delay
"""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
     Spawn wait_random n times with the specified max_delay

     Args:
        n (int): Nimber of times to swap task_wait_random
        max_delay (int):
    Returns:
        float: list of all the delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    #  Gether the results in the order they complete
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)
