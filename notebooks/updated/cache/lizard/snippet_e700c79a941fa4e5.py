def v2010(self):
    if self._v2010 is None:
        self._v2010 = V2010(self)
    return self._v2010