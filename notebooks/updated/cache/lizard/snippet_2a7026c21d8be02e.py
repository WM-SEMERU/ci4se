def cublasCreate():
    handle = ctypes.c_void_p()
    status = _libcublas.cublasCreate_v2(ctypes.byref(handle))
    cublasCheckStatus(status)
    return handle.value