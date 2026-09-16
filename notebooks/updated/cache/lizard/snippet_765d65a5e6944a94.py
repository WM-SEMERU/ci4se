def colormapper(value, lower=0, upper=1, cmap=None):
    cmap = get_cmap(cmap)
    if upper - lower == 0:
        rgba = cmap(0)
    else:
        rgba = cmap((value - lower) / float(upper - lower))
    hex_ = rgb2hex(rgba)
    return hex_