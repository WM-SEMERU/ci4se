def cachedstr(self):
    if self._cachedstr is None:
        if self.module is not None:
            refstring = self.module.refstring
            self._cachedstr = refstring.splitlines()
        else:
            self._cachedstr = []
    return self._cachedstr