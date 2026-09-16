def run_coroutine_threadsafe(self, coro, loop=None, callback=None):
    if not asyncio.iscoroutine(coro):
        raise TypeError('A await in coroutines. object is required')
    loop = loop or self.loop
    future = NewFuture(callback=callback)

    def callback_func():
        try:
            asyncio.futures._chain_future(NewTask(coro, loop=loop), future)
        except Exception as exc:
            if future.set_running_or_notify_cancel():
                future.set_exception(exc)
            raise
    loop.call_soon_threadsafe(callback_func)
    return future