def from_defaults(clz, defaults):
    if isinstance(defaults, (str, unicode)):
        defaults = json.loads(defaults)
    c = clz()
    for attribute in defaults.keys():
        if attribute in c:
            value = defaults[attribute]
            c[attribute].merge(value)
    cr = clz.random()
    for attribute, value in cr:
        try:
            c[attribute].merge(value)
        except Contradiction:
            pass
    return c