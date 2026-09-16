def parse(cls, fptr, offset, length):
    num_bytes = offset + length - fptr.tell()
    read_buffer = fptr.read(num_bytes)
    the_uuid = UUID(bytes=read_buffer[0:16])
    return cls(the_uuid, read_buffer[16:], length=length, offset=offset)