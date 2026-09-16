async def _execute(self, fn, *args, **kwargs):
    function = partial(fn, *args, **kwargs)
    future = self._loop.create_future()
    self._tx.put_nowait((future, function))
    return await future