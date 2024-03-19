#!/usr/bin/env python3

"""
Execute async_comprehension four times in parallel using asyncio.gather
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather

    Returns:
        Total runtime
    """
    #  record start time
    start_time = asyncio.get_event_loop().time()

    #  execute async_comprehension four 4 times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    #  record end time
    end_time = asyncio.get_event_loop().time()

    total_runtime = end_time - start_time

    return total_runtime
