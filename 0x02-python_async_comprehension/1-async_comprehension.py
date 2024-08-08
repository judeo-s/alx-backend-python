#!/usr/bin/env python3

"""
A python script that generates a list asynchronously
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An async function that yields a random number between 0 - 10
    """
    return [i async for i in async_generator()]
