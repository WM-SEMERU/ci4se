def click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=
    0.0, tween=linear, pause=None, _pause=True):
    if button not in ('left', 'middle', 'right', 1, 2, 3):
        raise ValueError(
            "button argument must be one of ('left', 'middle', 'right', 1, 2, 3)"
            )
    _failSafeCheck()
    x, y = _unpackXY(x, y)
    _mouseMoveDrag('move', x, y, 0, 0, duration, tween)
    x, y = platformModule._position()
    for i in range(clicks):
        _failSafeCheck()
        if button == 1 or str(button).lower() == 'left':
            platformModule._click(x, y, 'left')
        elif button == 2 or str(button).lower() == 'middle':
            platformModule._click(x, y, 'middle')
        elif button == 3 or str(button).lower() == 'right':
            platformModule._click(x, y, 'right')
        else:
            platformModule._click(x, y, button)
        time.sleep(interval)
    _autoPause(pause, _pause)