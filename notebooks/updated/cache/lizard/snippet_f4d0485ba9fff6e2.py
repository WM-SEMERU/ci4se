def batch(byte_array, funcs):
    result = []
    length = bytes_to_int(byte_array[0:4])
    item_size = bytes_to_int(byte_array[4:8])
    for i in range(0, length):
        chunk = byte_array[8 + i * item_size:8 + (i + 1) * item_size]
        for f in funcs:
            f(chunk)
    return result