def detach(self):
    from . import _ndarray_cls
    hdl = NDArrayHandle()
    check_call(_LIB.MXNDArrayDetach(self.handle, ctypes.byref(hdl)))
    return _ndarray_cls(hdl)