def cancel(self, cancel_running=True, mark_completed_as_cancelled=False):
    with self._lock:
        for future in self._queue:
            future.cancel(mark_completed_as_cancelled)
        if cancel_running:
            for future in self._running:
                future.cancel(mark_completed_as_cancelled)
        self._queue.clear()