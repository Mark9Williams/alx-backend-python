#!/usr/bin/env python3
"""Asynchronous coroutine that returns a list of delays"""

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


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine that takes in 2 arguments and returns a list of delays"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        delays.append(result)
    return delays
