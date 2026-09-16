def write(bar, offset, data):
    if type(data) not in [bytes, bytearray]:
        msg = 'data should be bytes or bytearray type'
        raise TypeError(msg)
    size = len(data)
    verify_access_range(bar, offset, size)
    if bar.type == 'io':
        return io_write(bar, offset, data)
    if bar.type == 'mem':
        return mem_write(bar, offset, data)
    return