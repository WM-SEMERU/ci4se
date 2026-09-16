def quit(self, *args, **kwargs):
    self._stop = True
    super(ReadProbes, self).quit(*args, **kwargs)