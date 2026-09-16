def hscroll(clicks, x=None, y=None, pause=None, _pause=True):
    _failSafeCheck()
    if type(x) in (tuple, list):
        x, y = x[0], x[1]
    x, y = position(x, y)
    platformModule._hscroll(clicks, x, y)
    _autoPause(pause, _pause)