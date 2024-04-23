#!/usr/bin/env python3
"""
Tasks Module
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that waits for a random amount of time
    (0 to max_delay) and returns the result.
    """
    return asyncio.create_task(wait_random(max_delay))
