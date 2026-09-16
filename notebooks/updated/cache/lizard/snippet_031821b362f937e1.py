def type(self):
    kv_type = ctypes.c_char_p()
    check_call(_LIB.MXKVStoreGetType(self.handle, ctypes.byref(kv_type)))
    return py_str(kv_type.value)