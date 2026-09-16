def pack(cls, data):
    return struct.pack('>ll', len(data) + 4, cls.FRAME_TYPE) + data