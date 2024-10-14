#!/usr/bin/env python3
"""Measure the runtime of wait_n"""

import asyncio
import time
import importlib.util


# Load 1-concurrent_coroutines.py dynamically
spec_concurrent = importlib.util.spec_from_file_location(
    "concurrent_coroutines", "./1-concurrent_coroutines.py")
concurrent_module = importlib.util.module_from_spec(spec_concurrent)
spec_concurrent.loader.exec_module(concurrent_module)

# Access wait_random and wait_n from the dynamically loaded modules
wait_n = concurrent_module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
