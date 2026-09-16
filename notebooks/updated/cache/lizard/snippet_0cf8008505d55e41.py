def option2tuple(opt):
    if isinstance(opt[0], int):
        tup = opt[1], opt[2:]
    else:
        tup = opt[0], opt[1:]
    return tup