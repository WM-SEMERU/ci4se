def GetSize(cls):
    format_str = ''.join([x[0] for x in cls._fields])
    return struct.calcsize(format_str)