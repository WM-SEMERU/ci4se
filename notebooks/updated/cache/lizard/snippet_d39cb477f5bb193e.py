def list_arguments(self):
    size = ctypes.c_uint()
    sarr = ctypes.POINTER(ctypes.c_char_p)()
    check_call(_LIB.MXSymbolListArguments(self.handle, ctypes.byref(size),
        ctypes.byref(sarr)))
    return [py_str(sarr[i]) for i in range(size.value)]