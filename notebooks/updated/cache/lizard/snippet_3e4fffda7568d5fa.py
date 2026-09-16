def hexdump(self, s, *args, **kwargs):
    levelOverride = kwargs.get('level') or self._lastlevel
    hexdmp = hexdump.hexdump(self, s, **kwargs)
    self._log(levelOverride, hexdmp, 'indented', args, kwargs)