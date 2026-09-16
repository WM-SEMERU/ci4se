def get(self):
    if self._index is None:
        raise HDF4Error('non existent attribute')
    status, aName, data_type, n_values, size = _C.Vattrinfo(self._v_inst.
        _id, self._index)
    _checkErr('get', status, 'illegal parameters')
    convert = _array_to_ret
    if data_type == HC.CHAR8:
        buf = _C.array_byte(n_values)
        convert = _array_to_str
    elif data_type in [HC.UCHAR8, HC.UINT8]:
        buf = _C.array_byte(n_values)
    elif data_type == HC.INT8:
        buf = _C.array_int8(n_values)
    elif data_type == HC.INT16:
        buf = _C.array_int16(n_values)
    elif data_type == HC.UINT16:
        buf = _C.array_uint16(n_values)
    elif data_type == HC.INT32:
        buf = _C.array_int32(n_values)
    elif data_type == HC.UINT32:
        buf = _C.array_uint32(n_values)
    elif data_type == HC.FLOAT32:
        buf = _C.array_float32(n_values)
    elif data_type == HC.FLOAT64:
        buf = _C.array_float64(n_values)
    else:
        raise HDF4Error(
            'get: attribute index %d has an illegal or unupported type %d' %
            (self._index, data_type))
    status = _C.Vgetattr(self._v_inst._id, self._index, buf)
    _checkErr('get', status, 'illegal attribute ')
    return convert(buf, n_values)