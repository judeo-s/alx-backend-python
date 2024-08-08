#!/usr/bin/env python3

"""
A python script that times asynchronous tasks
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    An async function that tracks the execution time of 4 asynchronous tasks
    """
    start = time.time()
    task_list = [
            asyncio.create_task(async_comprehension()) for _ in range(4)
            ]
    await asyncio.gather(*task_list)
    end = time.time()
    return (end - start)
