def reconnect(self):
    self.connect(*self._saved_connect.args, **self._saved_connect.kwargs)