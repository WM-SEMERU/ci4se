def elementTypeName(self):
    if self._array is None:
        return super(ArrayRti, self).elementTypeName
    else:
        dtype = self._array.dtype
        return '<structured>' if dtype.names else str(dtype)