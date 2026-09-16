def read_uint(data, start, length):
    return int.from_bytes(data[start:start + length], byteorder='big')