#!/usr/bin/env python3
"""
Measure Runtime Module
"""

import asyncio
from time import perf_counter
from typing import List
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing async_comprehension
    four times in parallel.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = perf_counter()

    return end_time - start_time
