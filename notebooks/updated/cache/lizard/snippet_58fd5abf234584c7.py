def stop(self):
    if self._stack:
        try:
            self._stack.teardown()
        except Exception:
            self.fatal(sys.exc_info())
    super().stop()