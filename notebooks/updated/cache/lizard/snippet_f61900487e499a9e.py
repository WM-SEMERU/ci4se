def timedelta_to_seconds(delta):
    if delta.microseconds:
        total = delta.microseconds * 1e-06
    else:
        total = 0
    total += delta.seconds
    total += delta.days * 60 * 60 * 24
    return total