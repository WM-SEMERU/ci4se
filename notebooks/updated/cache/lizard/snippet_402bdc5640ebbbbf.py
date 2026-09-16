def get(self):
    if self._index is None:
        try:
            self._index = self._obj.findattr(self._name)
        except HDF4Error:
            raise HDF4Error('get: cannot convert name to index')
    status, self._name, data_type, n_values = _C.SDattrinfo(self._obj._id,
        self._index)
    _checkErr('read', status, 'illegal attribute index')
    convert = _array_to_ret
    if data_type == SDC.CHAR8:
        buf = _C.array_byte(n_values)
        convert = _array_to_str
    elif data_type in [SDC.UCHAR8, SDC.UINT8]:
        buf = _C.array_byte(n_values)
    elif data_type == SDC.INT8:
        buf = _C.array_int8(n_values)
    elif data_type == SDC.INT16:
        buf = _C.array_int16(n_values)
    elif data_type == SDC.UINT16:
        buf = _C.array_uint16(n_values)
    elif data_type == SDC.INT32:
        buf = _C.array_int32(n_values)
    elif data_type == SDC.UINT32:
        buf = _C.array_uint32(n_values)
    elif data_type == SDC.FLOAT32:
        buf = _C.array_float32(n_values)
    elif data_type == SDC.FLOAT64:
        buf = _C.array_float64(n_values)
    else:
        raise HDF4Error(
            'read: attribute index %d has an illegal or unupported type %d' %
            (self._index, data_type))
    status = _C.SDreadattr(self._obj._id, self._index, buf)
    _checkErr('read', status, 'illegal attribute index')
    return convert(buf, n_values)