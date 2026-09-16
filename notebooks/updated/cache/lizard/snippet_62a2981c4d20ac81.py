def ReadTag(buffer, pos):
    start = pos
    while six.indexbytes(buffer, pos) & 128:
        pos += 1
    pos += 1
    return buffer[start:pos], pos