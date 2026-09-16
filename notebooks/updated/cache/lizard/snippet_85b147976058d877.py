def bind(self, isnap, istep):
    self._isteps[isnap] = istep
    self.sdat.steps[istep].isnap = isnap