#!/usr/bin/env python3

"""
A python script that generates a list asynchronously
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An async function that yields a random number between 0 - 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
