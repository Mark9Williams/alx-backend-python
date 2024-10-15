#!/usr/bin/env python3
"""Async generator that yields random numbers between 0 and 10."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields a random float between 0 and 10, 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
