def _read_bytes(fp, buf):
    offset = 0
    remaining = len(buf)
    while remaining > 0:
        l = fp.readinto((ctypes.c_char * remaining).from_buffer(buf, offset))
        if l is None or l == 0:
            return offset
        offset += l
        remaining -= l
    return offset