def _encode_mapping(name, value, check_keys, opts):
    data = b''.join([_element_to_bson(key, val, check_keys, opts) for key,
        val in iteritems(value)])
    return b'\x03' + name + _PACK_INT(len(data) + 5) + data + b'\x00'