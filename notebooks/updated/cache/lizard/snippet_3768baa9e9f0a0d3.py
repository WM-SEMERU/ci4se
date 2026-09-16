def RgbToIntTuple(r, g, b):
    return tuple(int(round(v * 255)) for v in (r, g, b))