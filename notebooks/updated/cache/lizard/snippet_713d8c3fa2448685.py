def _dump_point(obj, decimals):
    coords = obj['coordinates']
    pt = 'POINT (%s)' % ' '.join(_round_and_pad(c, decimals) for c in coords)
    return pt