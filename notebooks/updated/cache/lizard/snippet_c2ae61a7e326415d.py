def stop(self, timeout=None):
    if timeout is not None:
        log.warning(
            'timeout argument to stop() is deprecated - it will be removed in future release'
            )
    if not self.async_send:
        log.warning('producer.stop() called, but producer is not async')
        return
    if self.stopped:
        log.warning('producer.stop() called, but producer is already stopped')
        return
    if self.async_send:
        self.queue.put((STOP_ASYNC_PRODUCER, None, None))
        self.thread_stop_event.set()
        self.thread.join()
    if hasattr(self, '_cleanup_func'):
        if hasattr(atexit, 'unregister'):
            atexit.unregister(self._cleanup_func)
        else:
            try:
                atexit._exithandlers.remove((self._cleanup_func, (self,), {}))
            except ValueError:
                pass
        del self._cleanup_func
    self.stopped = True