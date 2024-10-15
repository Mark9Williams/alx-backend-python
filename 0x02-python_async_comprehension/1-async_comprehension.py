#!/usr/bin/env python3
"""Async Comprehensions module"""

import asyncio
import importlib.util
from typing import List

# Dynamically load the module with unconventional name
spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-async_generator.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can access async_generator from the loaded module
async_generator = module.async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing"""
    return [i async for i in async_generator()]
