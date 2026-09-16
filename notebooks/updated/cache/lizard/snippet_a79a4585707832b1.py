def hex_to_int(value):
    if version_info.major >= 3:
        return int.from_bytes(value, 'big')
    return int(value.encode('hex'), 16)