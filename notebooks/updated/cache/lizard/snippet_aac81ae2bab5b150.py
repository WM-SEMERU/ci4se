def _future_command_unlocked(self, cmd):
    future = self._loop.create_future()
    asyncio_loop = self._loop.get_loop()

    def _done_callback(result):
        retval = result['return_value']
        if not result['result']:
            future.set_exception(HardwareError(
                'Error executing synchronous command', command=cmd,
                return_value=retval))
        else:
            future.set_result(retval)
    callback = functools.partial(asyncio_loop.call_soon_threadsafe,
        _done_callback)
    self._commands.put((cmd, callback, True, None))
    return future