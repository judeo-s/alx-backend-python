#!/usr/bin/env python3

"""
A python3 script to measure the approximate time of execution for each
asycronous function.
"""

import time
import asyncio
from typing import Callable
wait_n: Callable = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function to measure the time of an async function
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
