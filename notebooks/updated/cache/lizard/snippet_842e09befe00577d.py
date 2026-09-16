def as_timedelta(cls, delta):
    if isinstance(delta, cls):
        return delta
    return cls(delta.days, delta.seconds, delta.microseconds)