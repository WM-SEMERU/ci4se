def read_plain_float(file_obj, count):
    return struct.unpack('<{}f'.format(count).encode('utf-8'), file_obj.
        read(4 * count))