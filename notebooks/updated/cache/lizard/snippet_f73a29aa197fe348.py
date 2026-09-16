def info(self):
    buf = _C.array_int32(_C.H4_MAX_VAR_DIMS)
    status, sds_name, rank, data_type, n_attrs = _C.SDgetinfo(self._id, buf)
    _checkErr('info', status, 'cannot execute')
    dim_sizes = _array_to_ret(buf, rank)
    return sds_name, rank, dim_sizes, data_type, n_attrs