#!/usr/bin/env python3
"""Module to create asyncio.Task from wait_random function"""

import asyncio
import importlib.util

# Load 0-basic_async_syntax.py dynamically
spec = importlib.util.spec_from_file_location(
    "basic_async_syntax", "./0-basic_async_syntax.py")
basic_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic_module)

# Access wait_random from the dynamically loaded module
wait_random = basic_module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an asyncio.Task."""
    task = asyncio.create_task(wait_random(max_delay))
    return task
