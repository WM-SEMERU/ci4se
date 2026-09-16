def move_arc(x, y, r, speed=1, orientation=True):
    _x, _y = win32api.GetCursorPos()
    c_len = (r ** 2 - (((x - _x) / 2) ** 2 + ((y - _y) / 2) ** 2)) ** 0.5
    t = (c_len ** 2 / ((y - _y) ** 2 + (x - _x) ** 2)) ** 0.5
    t = t if orientation else -t
    centre = (_x + x) / 2 + t * (_x - x), (_y + y) / 2 + t * (y - _y)
    if any(isinstance(ordinate, complex) for ordinate in centre):
        raise ValueError('Radius too low - minimum: {}'.format(((x - _x) **
            2 + (y - _y) ** 2) ** 0.5 / 2))
    theta = math.atan2(_y - centre[1], _x - centre[0])
    end = math.atan2(y - centre[1], x - centre[0])
    while theta < end:
        move(*list(map(round, (centre[0] + r * math.cos(theta), centre[1] +
            r * math.sin(theta)))))
        theta += speed / 100
        time.sleep(0.01)
    move(x, y)