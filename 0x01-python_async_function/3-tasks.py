#!/usr/bin/env python3

"""
A python3 script to return an asyncio.Task object
"""

import asyncio
from typing import Callable

wait_random: Callable = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function returns an asyncio.Task object from the wait_random function
    """

    return asyncio.create_task(wait_random(max_delay))
