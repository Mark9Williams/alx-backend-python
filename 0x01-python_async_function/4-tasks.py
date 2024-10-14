#!/usr/bin/env python3
"""Module to execute multiple asyncio.Tasks using task_wait_random"""

import asyncio
from typing import List
import importlib.util

# Dynamically load the module with unconventional name
spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can access wait_random from the loaded module
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns an asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    # Gather results as tasks complete
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
