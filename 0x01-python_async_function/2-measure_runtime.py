#!/usr/bin/env python3

"""
Measures the total execution time for wait_n(n, max_delay)
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of time to call wait_n
        max_delay (int): maximum delay for each wait_random call

    Returns:
        float: total_time / n
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
