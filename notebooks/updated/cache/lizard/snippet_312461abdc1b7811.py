async def is_try_or_pull_request(self):
    tasks = [asyncio.ensure_future(link.is_try_or_pull_request()) for link in
        self.links]
    tasks.insert(0, asyncio.ensure_future(is_try_or_pull_request(self.
        context, self.task)))
    conditions = await raise_future_exceptions(tasks)
    return any(conditions)