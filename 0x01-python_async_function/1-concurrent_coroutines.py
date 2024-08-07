#!/usr/bin/env python3

"""
A python script to learn about asyncronous programming
"""

import asyncio
import random
from typing import List, Callable

wait_random: Callable = __import__('0-basic_async_syntax').wait_random

async wait_n(n: int, max_delay: int):
    delays: List[float] = [
            asyncio.create_task(wait_random(max_delay)) for _ in range(n)
            ]
    return [await delay for delay in asyncio.as_completed(delays)]
