def emit(self, event, *args, **kwargs):
    self._emit(event, self, *args, **kwargs)