def start(self):
    if not self._started:
        self.sig_started.emit(self)
        self._started = True