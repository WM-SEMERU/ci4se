def emit_function(self, return_type=None, argtypes=[], proxy=True):
    if argtypes is not None:
        make_func = ctypes.CFUNCTYPE(return_type, *argtypes)
    else:
        make_func = ctypes.CFUNCTYPE(return_type)
    code = self.emit()
    func = make_func(code.value)
    func.address = code
    if proxy:
        self.functions.append(func)
        return weakref.proxy(func)
    else:
        return func