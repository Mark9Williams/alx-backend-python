#!/usr/bin/env python3
"""Asynchronous coroutine that returns a list of delays"""

import asyncio
from typing import List
import importlib.util

# Dynamically load the module with unconventional name
spec_concurrent = importlib.util.spec_from_file_location(
    "concurrent_coroutines", "./3-tasks.py")
module = importlib.util.module_from_spec(spec_concurrent)
spec_concurrent.loader.exec_module(module)

# Now you can access wait_random from the loaded module
wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay."""
    tasks = [task_wait_n(n, max_delay) for _ in range(n)]
    delays = []

    # Gather results as tasks complete
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
