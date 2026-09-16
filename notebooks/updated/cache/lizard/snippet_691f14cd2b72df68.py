def setColumn(self, header, values):
    if any(isinstance(value, basestring) for value in values):
        values = list(map(str, values))
        self._impl.setColumnStr(header, values, len(values))
    elif all(isinstance(value, Real) for value in values):
        values = list(map(float, values))
        self._impl.setColumnDbl(header, values, len(values))
    else:
        print(values)
        raise NotImplementedError