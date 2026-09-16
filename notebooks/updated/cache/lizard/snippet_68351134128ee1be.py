def load_arrays(self, v, f):
    if not isinstance(v, np.ndarray):
        try:
            v = np.asarray(v, np.float)
            if v.ndim != 2 and v.shape[1] != 3:
                raise Exception('Invalid vertex format.  Shape ' +
                    'should be (npoints, 3)')
        except BaseException:
            raise Exception(
                'Unable to convert vertex input to valid numpy array')
    if not isinstance(f, np.ndarray):
        try:
            f = np.asarray(f, ctypes.c_int)
            if f.ndim != 2 and f.shape[1] != 3:
                raise Exception('Invalid face format.  ' +
                    'Shape should be (nfaces, 3)')
        except BaseException:
            raise Exception('Unable to convert face input to valid' +
                ' numpy array')
    self.v = v
    self.f = f