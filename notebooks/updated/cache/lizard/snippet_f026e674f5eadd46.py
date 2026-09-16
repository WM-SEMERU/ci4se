def _got_cons_input(self, handle):
    self._addpendingdata(handle.read())
    if not self.awaitingack:
        self._sendpendingoutput()