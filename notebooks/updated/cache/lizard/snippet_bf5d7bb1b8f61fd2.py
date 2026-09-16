def unpack_rows(rows):
    for row in rows:
        fmt = '!%dH' % len(row)
        yield bytearray(struct.pack(fmt, *row))