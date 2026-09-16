def hex2rgb(str_rgb):
    try:
        rgb = str_rgb[1:]
        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError('Invalid value %r provided for rgb color.' % str_rgb)
    return tuple([(float(int(v, 16)) / 255) for v in (r, g, b)])