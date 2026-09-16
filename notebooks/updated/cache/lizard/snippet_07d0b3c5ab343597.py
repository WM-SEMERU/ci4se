def set_referencevalue(self, val):
    assert len(val) == len(self._coord['crval'])
    self._coord['crval'] = val[::-1]