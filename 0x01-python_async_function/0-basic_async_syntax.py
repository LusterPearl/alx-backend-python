#!/usr/bin/env python3
"""
Module for asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchtonous coroutin that awaits for a random dealy between
    Args:
        max_delay (int): The maximum delay in seconds

    Return:
        float: The random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay