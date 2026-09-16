async def run(self, kwargs=None):
    task = self._prepare(kwargs)
    try:
        await task
    except Exception as e:
        raise e