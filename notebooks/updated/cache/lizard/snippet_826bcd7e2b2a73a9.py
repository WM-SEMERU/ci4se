def fitted(self, fid=0):
    self._checkid(fid)
    return not (self._fitids[fid]['fit'] > 0 or self._fitids[fid]['fit'] < 
        -0.001)