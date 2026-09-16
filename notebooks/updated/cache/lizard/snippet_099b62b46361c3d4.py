def get(self, name):
    pm = self._libeng.engGetVariable(self._ep, name)
    out = mxarray_to_ndarray(self._libmx, pm)
    self._libmx.mxDestroyArray(pm)
    return out