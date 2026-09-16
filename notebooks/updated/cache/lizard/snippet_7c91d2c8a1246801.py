def dumpJSON(self):
    g = get_root(self).globals
    return dict(RA=self.ra['text'], DEC=self.dec['text'], tel=g.cpars[
        'telins_name'], alt=self._getVal(self.alt), az=self._getVal(self.az
        ), secz=self._getVal(self.airmass), pa=self._getVal(self.pa), foc=
        self._getVal(self.focus), mdist=self._getVal(self.mdist))