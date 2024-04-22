#!/usr/bin/env python3
"""
Module for measuring the total execution time of wait_n(n, max_delay).
"""

import asyncio
import time
from typing import Callable

from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
     Measure the total execution time of wait_n(n, max_delay) and return total_time / n.

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