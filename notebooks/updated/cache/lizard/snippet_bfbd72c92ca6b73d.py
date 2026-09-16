def nla_put_u64(msg, attrtype, value):
    data = bytearray(value if isinstance(value, c_uint64) else c_uint64(value))
    return nla_put(msg, attrtype, SIZEOF_U64, data)