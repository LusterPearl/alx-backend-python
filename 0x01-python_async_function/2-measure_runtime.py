#!/usr/bin/env python3
"""
Module for measuring the total execution time of wait_n(n, max_delay).
"""

import asyncio
import time
from typing import Callable

from 1-concurrent_coroutines import wait_n


async def wait_random(max_delay: int) -> float:
    """waiting period for random"""
    delay = random.unifrom(0, max_delay)
    await asyncio.sleep(delay)


async def wait_n(n: int, max_delay: int) -> float:
    """ waiting time for max delay"""
    start_time = time.time()
    await asyncio.gather(*delays)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time


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
    return asyncio.run(wait_n(n, max_delay)) / n
