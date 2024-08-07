#!/usr/bin/env python3

"""
A script to ascyncronously generate random delay times
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function returns a random float number between 0 and max_delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
