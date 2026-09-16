def translate(patterns, *, flags=0):
    flags = _flag_transform(flags)
    return _wcparse.translate(_wcparse.split(patterns, flags), flags)