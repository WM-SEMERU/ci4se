def __init_from_csr(self, csr, params_str, ref_dataset):
    if len(csr.indices) != len(csr.data):
        raise ValueError('Length mismatch: {} vs {}'.format(len(csr.indices
            ), len(csr.data)))
    self.handle = ctypes.c_void_p()
    ptr_indptr, type_ptr_indptr, __ = c_int_array(csr.indptr)
    ptr_data, type_ptr_data, _ = c_float_array(csr.data)
    assert csr.shape[1] <= MAX_INT32
    csr.indices = csr.indices.astype(np.int32, copy=False)
    _safe_call(_LIB.LGBM_DatasetCreateFromCSR(ptr_indptr, ctypes.c_int(
        type_ptr_indptr), csr.indices.ctypes.data_as(ctypes.POINTER(ctypes.
        c_int32)), ptr_data, ctypes.c_int(type_ptr_data), ctypes.c_int64(
        len(csr.indptr)), ctypes.c_int64(len(csr.data)), ctypes.c_int64(csr
        .shape[1]), c_str(params_str), ref_dataset, ctypes.byref(self.handle)))
    return self