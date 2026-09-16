def error_future(self):
    fut = asyncio.Future(loop=self._loop)
    self._error_futures.append(fut)
    return fut