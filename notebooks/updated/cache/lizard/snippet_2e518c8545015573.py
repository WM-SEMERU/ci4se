def CreateNumpyVector(self, x):
    if np is None:
        raise NumpyRequiredForThisFeature('Numpy was not found.')
    if not isinstance(x, np.ndarray):
        raise TypeError('non-numpy-ndarray passed to CreateNumpyVector')
    if x.dtype.kind not in ['b', 'i', 'u', 'f']:
        raise TypeError('numpy-ndarray holds elements of unsupported datatype')
    if x.ndim > 1:
        raise TypeError('multidimensional-ndarray passed to CreateNumpyVector')
    self.StartVector(x.itemsize, x.size, x.dtype.alignment)
    if x.dtype.str[0] == '<':
        x_lend = x
    else:
        x_lend = x.byteswap(inplace=False)
    l = UOffsetTFlags.py_type(x_lend.itemsize * x_lend.size)
    self.head = UOffsetTFlags.py_type(self.Head() - l)
    self.Bytes[self.Head():self.Head() + l] = x_lend.tobytes(order='C')
    return self.EndVector(x.size)