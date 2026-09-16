def set_functions(self, f='a*x*cos(b*x)+c', p='a=-0.2, b, c=3', c=None, bg=
    None, **kwargs):
    self._pnames = []
    self._cnames = []
    self._pguess = []
    self._constants = []
    self._globals.update(kwargs)
    self._f_raw = f
    self._bg_raw = bg
    if c:
        for s in c.split(','):
            s = s.split('=')
            self._cnames.append(s[0].strip())
            if len(s) > 1:
                self._constants.append(float(s[1]))
            else:
                self._constants.append(1.0)
    for s in p.split(','):
        s = s.split('=')
        self._pnames.append(s[0].strip())
        if len(s) > 1:
            self._pguess.append(float(s[1]))
        else:
            self._pguess.append(1.0)
    self._update_functions()
    if self['autoplot']:
        self.plot()
    return self