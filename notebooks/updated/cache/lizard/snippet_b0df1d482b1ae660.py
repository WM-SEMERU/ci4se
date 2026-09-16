def set_default(cls, name):
    if name not in cls._depots:
        raise RuntimeError('%s depot has not been configured' % (name,))
    cls._default_depot = name