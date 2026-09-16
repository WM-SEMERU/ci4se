def on_stop(self):
    LOGGER.debug('natsd.Service.on_stop')
    self.is_started = False
    try:
        next(self.nc.unsubscribe(self.serviceQS))
    except StopIteration as e:
        pass
    try:
        next(self.nc.close())
    except StopIteration as e:
        pass
    try:
        for task in asyncio.Task.all_tasks(self.loop):
            task.cancel()
        self.loop.stop()
        while self.loop.is_running():
            time.sleep(1)
        self.loop.close()
    except Exception as e:
        LOGGER.debug('natsd.Service.on_stop - Exception aio clean up : ' +
            traceback.format_exc())