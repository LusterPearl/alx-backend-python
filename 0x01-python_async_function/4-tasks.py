#!/usr/bin/env python3
"""
Module for creating asyncio.Task objects for multiple coroutines.
"""

import asyncio
import random
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """Asynchronous coroutine that waits for a random delay between 0
       and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay.
        """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task object that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object.
        """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create and run asyncio.Task objects for wait_random n times with the
        specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random tasks.
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
        """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
