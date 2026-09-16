def create_span(unirange, is_bytes=False):
    if len(unirange) < 2:
        unirange.append(unirange[0])
    if is_bytes:
        if unirange[0] > MAXASCII:
            return None
        if unirange[1] > MAXASCII:
            unirange[1] = MAXASCII
    return [x for x in range(unirange[0], unirange[1] + 1)]