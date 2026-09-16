def parse_geometry(geometry, ratio=None):
    m = geometry_pat.match(geometry)

    def syntax_error():
        return ThumbnailParseError(
            'Geometry does not have the correct syntax: %s' % geometry)
    if not m:
        raise syntax_error()
    x = m.group('x')
    y = m.group('y')
    if x is None and y is None:
        raise syntax_error()
    if x is not None:
        x = int(x)
    if y is not None:
        y = int(y)
    if ratio is not None:
        ratio = float(ratio)
        if x is None:
            x = toint(y * ratio)
        elif y is None:
            y = toint(x / ratio)
    return x, y