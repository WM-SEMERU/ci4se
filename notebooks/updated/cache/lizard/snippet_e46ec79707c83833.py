def _hex_to_rgb(hex_code):
    if len(hex_code) != 6:
        raise ValueError(hex_code +
            ' is not a string of length 6, cannot convert to rgb.')
    return tuple(map(ord, hex_code.decode('hex')))