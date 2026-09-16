def from_jd(jd, method=None):
    method = method or 'equinox'
    if method == 'equinox':
        return _from_jd_equinox(jd)
    else:
        return _from_jd_schematic(jd, method)