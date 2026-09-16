def ensure_fixed_length_bytes(var):
    dims, data, attrs, encoding = unpack_for_encoding(var)
    if check_vlen_dtype(data.dtype) == bytes:
        data = np.asarray(data, dtype=np.string_)
    return Variable(dims, data, attrs, encoding)