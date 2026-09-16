def __init_from_csc(self, csc, params_str, ref_dataset):
    if len(csc.indices) != len(csc.data):
        raise ValueError('Length mismatch: {} vs {}'.format(len(csc.indices
            ), len(csc.data)))
    self.handle = ctypes.c_void_p()
    ptr_indptr, type_ptr_indptr, __ = c_int_array(csc.indptr)
    ptr_data, type_ptr_data, _ = c_float_array(csc.data)
    assert csc.shape[0] <= MAX_INT32
    csc.indices = csc.indices.astype(np.int32, copy=False)
    _safe_call(_LIB.LGBM_DatasetCreateFromCSC(ptr_indptr, ctypes.c_int(
        type_ptr_indptr), csc.indices.ctypes.data_as(ctypes.POINTER(ctypes.
        c_int32)), ptr_data, ctypes.c_int(type_ptr_data), ctypes.c_int64(
        len(csc.indptr)), ctypes.c_int64(len(csc.data)), ctypes.c_int64(csc
        .shape[0]), c_str(params_str), ref_dataset, ctypes.byref(self.handle)))
    return self