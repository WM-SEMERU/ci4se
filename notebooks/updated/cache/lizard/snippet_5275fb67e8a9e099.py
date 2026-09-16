def SetMaxCurrent(self, i):
    if i < 0 or i > 8:
        raise MonsoonError(
            'Target max current %sA, is out of acceptable range [0, 8].' % i)
    val = 1023 - int(i / 8 * 1023)
    self._SendStruct('BBB', 1, 10, val & 255)
    self._SendStruct('BBB', 1, 11, val >> 8)