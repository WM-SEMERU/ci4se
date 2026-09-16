def get_symbol_size(version, scale=1, border=None):
    if border is None:
        border = get_default_border_size(version)
    dim = version * 4 + 17 if version > 0 else (version + 4) * 2 + 9
    dim += 2 * border
    dim *= scale
    return dim, dim