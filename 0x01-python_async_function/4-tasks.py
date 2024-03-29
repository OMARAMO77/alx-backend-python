#!/usr/bin/env python3
"""Tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times"""
    tasks_list = []
    delays_list = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks_list.append(task)

    for task in asyncio.as_completed((tasks_list)):
        delay = await task
        delays_list.append(delay)

    return delays_list
