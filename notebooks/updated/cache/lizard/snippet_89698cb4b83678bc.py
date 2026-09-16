async def process_updates(self, updates, fast: typing.Optional[bool]=True):
    if fast:
        tasks = []
        for update in updates:
            tasks.append(self.updates_handler.notify(update))
        return await asyncio.gather(*tasks)
    results = []
    for update in updates:
        results.append(await self.updates_handler.notify(update))
    return results