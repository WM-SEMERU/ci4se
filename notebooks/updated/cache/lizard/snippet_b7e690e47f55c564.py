def check_buffer(coords, length, buffer):
    s = min(coords[0], buffer)
    e = min(length - coords[1], buffer)
    return [s, e]