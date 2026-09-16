def _encode_secret_part_v2_v3(version, condition, root_key, ns):
    data = bytearray()
    data.append(version)
    encode_uvarint(len(root_key), data)
    data.extend(root_key)
    if version >= VERSION_3:
        encode_uvarint(len(ns), data)
        data.extend(ns)
    data.extend(condition.encode('utf-8'))
    return bytes(data)