def deprecation(self, message, *args, **kws):
    self._log(DEPRECATION, message, args, **kws)