def from_str(cls, coordinate):
    m = cls._coordinate_str_regex.match(coordinate)
    if m is None:
        raise ValueError('invalid coordinate string')
    if m.group(1) == '++':
        relative = True
    else:
        relative = False
    return TikZCoordinate(float(m.group(2)), float(m.group(4)), relative=
        relative)