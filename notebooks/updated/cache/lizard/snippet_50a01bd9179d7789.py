def tiff_header(read_buffer):
    data = struct.unpack('BB', read_buffer[0:2])
    if data[0] == 73 and data[1] == 73:
        endian = '<'
    elif data[0] == 77 and data[1] == 77:
        endian = '>'
    else:
        msg = (
            'The byte order indication in the TIFF header ({byte_order}) is invalid.  It should be either {little_endian} or {big_endian}.'
            )
        msg = msg.format(byte_order=read_buffer[6:8], little_endian=bytes([
            73, 73]), big_endian=bytes([77, 77]))
        raise IOError(msg)
    _, offset = struct.unpack(endian + 'HI', read_buffer[2:8])
    exif = ExifImageIfd(endian, read_buffer, offset)
    return exif.processed_ifd