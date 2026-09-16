def cudnnGetTensor4dDescriptor(tensorDesc):
    dataType = ctypes.c_int()
    n = ctypes.c_int()
    c = ctypes.c_int()
    h = ctypes.c_int()
    w = ctypes.c_int()
    nStride = ctypes.c_int()
    cStride = ctypes.c_int()
    hStride = ctypes.c_int()
    wStride = ctypes.c_int()
    status = _libcudnn.cudnnGetTensor4dDescriptor(tensorDesc, ctypes.byref(
        dataType), ctypes.byref(n), ctypes.byref(c), ctypes.byref(h),
        ctypes.byref(w), ctypes.byref(nStride), ctypes.byref(cStride),
        ctypes.byref(hStride), ctypes.byref(wStride))
    cudnnCheckStatus(status)
    return (dataType.value, n.value, c.value, h.value, w.value, nStride.
        value, cStride.value, hStride.value, wStride.value)