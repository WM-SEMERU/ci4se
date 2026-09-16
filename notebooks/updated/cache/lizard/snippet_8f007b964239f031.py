def sgr_fg_rgb(r, g, b):
    assert r in range(256)
    assert g in range(256)
    assert b in range(256)
    return '38;2;{};{};{}'.format(r, g, b)