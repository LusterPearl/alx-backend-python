#!/usr/bin/env python3
"""
Module for creating an asyncio.Task object.
"""

import asyncio
from typing import Any


def task_wait_random(max_delay: int) -> Any:
    """ Create an asyncio.Task object that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object.
        """
    return asyncio.create_task(wait_random(max_delay))


async def wait_random(max_delay: int) -> float:
    """Create an asyncio.Task object that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
