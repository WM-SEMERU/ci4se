def incr(name, value=1, rate=1, tags=None):
    client().incr(name, value, rate, tags)