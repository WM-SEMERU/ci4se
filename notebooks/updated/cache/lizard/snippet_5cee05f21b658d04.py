def stop(self, io_loop):
    running_async = False
    shutdown = _ShutdownHandler(io_loop)
    for callback in self.on_shutdown_callbacks:
        try:
            maybe_future = callback(self.tornado_application)
            if asyncio.iscoroutine(maybe_future):
                maybe_future = asyncio.create_task(maybe_future)
            if concurrent.is_future(maybe_future):
                shutdown.add_future(maybe_future)
                running_async = True
        except Exception as error:
            self.logger.warning(
                'exception raised from shutdown callback %r, ignored: %s',
                callback, error, exc_info=1)
    if not running_async:
        shutdown.on_shutdown_ready()