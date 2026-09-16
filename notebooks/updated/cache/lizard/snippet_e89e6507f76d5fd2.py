def smart_round(val, decimal_places=2):
    if isinstance(val, float) and val != 0.0:
        if val >= 10.0 ** -(decimal_places - 1):
            conv_str = ''.join(['%.', str(decimal_places), 'f'])
        else:
            conv_str = ''.join(['%.', str(decimal_places), 'e'])
        val = float(conv_str % val)
    return val