#!/usr/bin/env python3
"""
Module for measuring the total execution time of wait_n(n, max_delay).
"""

import asyncio
import time
import random


async def wait_random(max_delay: int) -> float:
    """waiting period for random"""
    delay = random.uniform(0, max_delay)
    time.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> float:
    """ waiting time for max delay"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)


def measure_time(n: int, max_delay: int) -> float:
    """
     Measure the total execution time of wait_n(n, max_delay)
     and return total_time / n.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        float: The average execution time per iteration.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
