def from_string(cls, s):
    s = s.strip()
    for i, char in enumerate(s):
        if char.isalpha() or char.isspace():
            break
    else:
        raise Exception('Unit is missing in string %s' % s)
    num, unit = float(s[:i]), s[i:]
    for unit_type, d in BASE_UNITS.items():
        if unit in d:
            break
    else:
        unit_type = None
    return cls(num, unit, unit_type=unit_type)