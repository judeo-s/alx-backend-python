#!/usr/bin/env python3

"""
A python script that generates a list asynchronously
"""
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """
    An async function that yields a random number between 0 - 10
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
