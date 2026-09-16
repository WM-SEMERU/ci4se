def _covert_to_hashable(data):
    r
    if isinstance(data, six.binary_type):
        hashable = data
        prefix = b'TXT'
    elif util_type.HAVE_NUMPY and isinstance(data, np.ndarray):
        if data.dtype.kind == 'O':
            msg = '[ut] hashing ndarrays with dtype=object is unstable'
            warnings.warn(msg, RuntimeWarning)
            hashable = data.dumps()
        else:
            hashable = data.tobytes()
        prefix = b'NDARR'
    elif isinstance(data, six.text_type):
        hashable = data.encode('utf-8')
        prefix = b'TXT'
    elif isinstance(data, uuid.UUID):
        hashable = data.bytes
        prefix = b'UUID'
    elif isinstance(data, int):
        hashable = _int_to_bytes(data)
        prefix = b'INT'
    elif util_type.HAVE_NUMPY and isinstance(data, np.int64):
        return _covert_to_hashable(int(data))
    elif util_type.HAVE_NUMPY and isinstance(data, np.float64):
        a, b = float(data).as_integer_ratio()
        hashable = a.to_bytes(8, byteorder='big') + b.to_bytes(8, byteorder
            ='big')
        prefix = b'FLOAT'
    else:
        raise TypeError('unknown hashable type=%r' % type(data))
    prefix = b''
    return prefix, hashable