async def set(self, *args, **kwargs):
    return await _maybe_await(self.event.set(*args, **kwargs))