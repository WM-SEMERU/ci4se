def stop(self):
    BufferedReader.stop(self)
    self._stop_running_event.set()
    self._writer_thread.join()
    BaseIOHandler.stop(self)