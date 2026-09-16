def _parse_rgn_segment(cls, fptr):
    offset = fptr.tell() - 2
    read_buffer = fptr.read(2)
    length, = struct.unpack('>H', read_buffer)
    nbytes = 3 if cls._csiz < 257 else 4
    fmt = '>BBB' if cls._csiz < 257 else '>HBB'
    read_buffer = fptr.read(nbytes)
    data = struct.unpack(fmt, read_buffer)
    length = length
    crgn = data[0]
    srgn = data[1]
    sprgn = data[2]
    return RGNsegment(crgn, srgn, sprgn, length, offset)