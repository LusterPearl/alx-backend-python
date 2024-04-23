#!/usr/bin/env python3
"""
Module for creating asyncio.Task objects for multiple coroutines.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delays sorted in ascending order.
    """
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(delays)