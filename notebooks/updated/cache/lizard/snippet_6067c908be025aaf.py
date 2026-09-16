def element_slice(self, start=None, stop=None, step=None):
    if self.dtype not in [str, array.array, list]:
        raise TypeError('SArray must contain strings, arrays or lists')
    with cython_context():
        return SArray(_proxy=self.__proxy__.subslice(start, step, stop))