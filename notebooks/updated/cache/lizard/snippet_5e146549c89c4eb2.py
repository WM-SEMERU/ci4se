def amint_to_char(am, hij=False, use_L=False):
    if use_L and am == [0, 1]:
        return 'l'
    if hij:
        amchar_map = _amchar_map_hij
    else:
        amchar_map = _amchar_map_hik
    amchar = []
    for a in am:
        if a < 0:
            raise IndexError(
                'Angular momentum must be a positive integer (not {})'.
                format(a))
        if a >= len(amchar_map):
            raise IndexError(
                'Angular momentum {} out of range. Must be less than {}'.
                format(a, len(amchar_map)))
        amchar.append(amchar_map[a])
    return ''.join(amchar)