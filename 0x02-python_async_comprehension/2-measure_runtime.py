#!/usr/bin/env python3
"""Measure runtime for async comprehension"""

import asyncio
import time
import importlib.util
from typing import List

# Dynamically load the async_comprehension function from the previous file
spec = importlib.util.spec_from_file_location(
    "async_comprehension", "./1-async_comprehension.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can access async_comprehension from the loaded module
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension run in parallel 4 times"""
    start_time = time.perf_counter()  # Record the start time

    # Run async_comprehension 4 times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time
