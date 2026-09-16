def send_complete(self):
    self.active = True
    if self.should_finish():
        self._detach()
        if not self._finished:
            self.safe_finish()
    elif self.session:
        self.session.flush()