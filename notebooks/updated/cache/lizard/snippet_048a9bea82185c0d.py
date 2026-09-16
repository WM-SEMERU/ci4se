def read_unsigned_var_int(file_obj):
    result = 0
    shift = 0
    while True:
        byte = struct.unpack(b'<B', file_obj.read(1))[0]
        result |= (byte & 127) << shift
        if byte & 128 == 0:
            break
        shift += 7
    return result