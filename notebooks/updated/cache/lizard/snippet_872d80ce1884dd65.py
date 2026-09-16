def _move_datetime(dt, direction, delta):
    if direction == 'next':
        dt = dt + delta
    elif direction == 'last':
        dt = dt - delta
    else:
        pass
    return dt