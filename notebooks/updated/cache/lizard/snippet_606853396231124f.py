def init_sdr(self):
    if self._sdr is None:
        self._sdr = sdr.SDR(self, self._sdrcachedir)
    return self._sdr