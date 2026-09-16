def periodic_callback(self):
    while True:
        try:
            action = self._deferred.get(False)
            action()
        except queue.Empty:
            break
        except Exception:
            self._logger.exception('Exception in periodic callback')