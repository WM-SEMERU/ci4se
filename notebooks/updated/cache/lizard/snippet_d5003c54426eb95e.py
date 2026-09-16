def set_float_info_npy2d(self, field, data):
    if getattr(data, 'base', None
        ) is not None and data.base is not None and isinstance(data, np.ndarray
        ) and isinstance(data.base, np.ndarray
        ) and not data.flags.c_contiguous:
        warnings.warn(
            'Use subset (sliced data) of np.ndarray is not recommended ' +
            'because it will generate extra copies and increase memory consumption'
            )
        data = np.array(data, copy=True, dtype=np.float32)
    else:
        data = np.array(data, copy=False, dtype=np.float32)
    c_data = data.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    _check_call(_LIB.XGDMatrixSetFloatInfo(self.handle, c_str(field),
        c_data, c_bst_ulong(len(data))))