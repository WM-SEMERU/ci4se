def parse_mode(mode, default_bitdepth=None):
    if mode == 'P':
        raise Error('Unknown colour mode:' + mode)
    elif mode == '1':
        return True, False, 1
    elif mode == 'I':
        return True, False, 16
    if mode.startswith('L'):
        grayscale = True
        mode = mode[1:]
    elif mode.startswith('RGB'):
        grayscale = False
        mode = mode[3:]
    else:
        raise Error('Unknown colour mode:' + mode)
    if mode.startswith('A'):
        alpha = True
        mode = mode[1:]
    else:
        alpha = False
    bitdepth = default_bitdepth
    if mode.startswith(';'):
        mode = mode[1:]
    if mode:
        try:
            bitdepth = int(mode)
        except (TypeError, ValueError):
            raise Error('Unsupported bitdepth mode:' + mode)
    return grayscale, alpha, bitdepth