def _SkipVarint(buffer, pos, end):
    while ord(buffer[pos:pos + 1]) & 128:
        pos += 1
    pos += 1
    if pos > end:
        raise _DecodeError('Truncated message.')
    return pos