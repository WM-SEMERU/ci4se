def stop(self):
    if self._started is False:
        raise ArgumentError(
            'EmulationLoop.stop() called without calling start()')
    self.verify_calling_thread(False,
        'Cannot call EmulationLoop.stop() from inside the event loop')
    if self._thread.is_alive():
        self._loop.call_soon_threadsafe(self._loop.create_task, self.
            _clean_shutdown())
        self._thread.join()