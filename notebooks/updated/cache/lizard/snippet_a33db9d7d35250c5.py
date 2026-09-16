def breakpoint(self, name):
    if name not in self._breakpoints:
        self.warning('Reached breakpoint %s but found no callback registered')
        return
    cb = self._breakpoints[name]
    cb.callback(None)
    return cb