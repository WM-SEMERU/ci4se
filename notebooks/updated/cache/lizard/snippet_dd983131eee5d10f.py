async def stop_tasks(self, address):
    tasks = self._tasks.get(address, [])
    for task in tasks:
        task.cancel()
    asyncio.gather(*tasks, return_exceptions=True)
    self._tasks[address] = []