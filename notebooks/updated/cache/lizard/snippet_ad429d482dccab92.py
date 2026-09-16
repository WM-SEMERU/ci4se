def stop(self):
    with self._lock:
        if self._stopped:
            _logger.debug('%s is already stopped', self)
            return
        self._flush_all_reports()
        self._stopped = True
        if self._run_scheduler_directly:
            self._cleanup_if_stopped()
        if self._scheduler and self._scheduler.empty():
            self._running = False
        self._scheduler = None