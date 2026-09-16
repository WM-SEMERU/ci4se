def bind_(cls, kls):
    if not hasattr(kls, '__call__'):
        raise TypeError("From Pylot.bind_: '%s' is not callable" % kls)
    cls._bind.add(kls)
    return kls