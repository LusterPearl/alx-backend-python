#!/usr/bin/env python3
"""
Module for creating an asyncio.Task object.
"""

import asyncio
import random
from typing import Any


from 0-basic_async_syntax import wait_random


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Any:
    """ Create an asyncio.Task object that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
