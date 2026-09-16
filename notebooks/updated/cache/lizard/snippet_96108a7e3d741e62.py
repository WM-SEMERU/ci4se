def set_host_def(self, hostdef):
    if self._hostdef is not None:
        self.info('Overwriting previous hostdef, which was %r', self._hostdef)
    self._hostdef = hostdef