def shape(self):
    shape_ptr = _ctypes.POINTER(_ctypes.c_size_t)()
    dim = _ctypes.c_size_t()
    status_code = self._LIB.TCMPSGetFloatArrayShape(self.handle, _ctypes.
        byref(shape_ptr), _ctypes.byref(dim))
    assert status_code == 0, 'Error calling TCMPSGetFloatArrayShape'
    return _shape_tuple_from_ctypes(shape_ptr, dim)