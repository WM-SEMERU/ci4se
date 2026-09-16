def int_to_rgba(cls, rgba_int):
    if rgba_int is None:
        return None, None, None, None
    alpha = rgba_int % 256
    blue = rgba_int / 256 % 256
    green = rgba_int / 256 / 256 % 256
    red = rgba_int / 256 / 256 / 256 % 256
    return red, green, blue, alpha