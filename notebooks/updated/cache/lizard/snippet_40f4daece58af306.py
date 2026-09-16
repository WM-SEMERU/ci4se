def parse_hex_color(value):
    if value.startswith('#'):
        value = value[1:]
    if len(value) == 3:
        return int(value[0] * 2, 16), int(value[1] * 2, 16), int(value[2] *
            2, 16)
    elif len(value) == 6:
        return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)
    else:
        raise ValueError()