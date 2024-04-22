#!/usr/bin/env python3
"""
Module for executing multiple coroutines at the same time with async.
"""


import asyncio
from typing import List
from random import uniform


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    synchronous coroutine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


async def wait_random(max_delay: int) -> float:
    """Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay.
        """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay