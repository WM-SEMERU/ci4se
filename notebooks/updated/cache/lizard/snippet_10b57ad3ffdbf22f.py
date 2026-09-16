def stop_periodic_snapshots(self):
    if self._periodic_thread and self._periodic_thread.isAlive():
        self._periodic_thread.stop = True
        self._periodic_thread.join()
        self._periodic_thread = None