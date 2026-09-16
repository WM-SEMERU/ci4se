def min(self):
    if self.is_quantized or self.base_dtype in (bool, string, complex64,
        complex128):
        raise TypeError('Cannot find minimum value of %s.' % self)
    try:
        return np.finfo(self.as_numpy_dtype()).min
    except:
        try:
            return np.iinfo(self.as_numpy_dtype()).min
        except:
            if self.base_dtype == bfloat16:
                return _np_bfloat16(float.fromhex('-0x1.FEp127'))
            raise TypeError('Cannot find minimum value of %s.' % self)