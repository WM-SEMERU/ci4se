def getBuffer(x):
    b = bytes(x)
    return (c_ubyte * len(b)).from_buffer_copy(bytes(x))