def parse(cls, buff, offset):
    primitive_struct = struct.Struct('!' + cls.fmt)
    value = primitive_struct.unpack_from(buff, offset)[0]
    offset += primitive_struct.size
    return value, offset