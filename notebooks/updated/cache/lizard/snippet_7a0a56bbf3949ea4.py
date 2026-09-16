def unit(self):
    unit = dataSetUnit(self._h5Dataset)
    fieldNames = self._h5Dataset.dtype.names
    if hasattr(unit, '__len__') and len(unit) == len(fieldNames):
        idx = fieldNames.index(self.nodeName)
        return unit[idx]
    else:
        return unit