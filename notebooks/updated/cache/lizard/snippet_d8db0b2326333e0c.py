def cmy_to_rgb(c, m=None, y=None):
    if type(c) in [list, tuple]:
        c, m, y = c
    return 1 - c, 1 - m, 1 - y