def nvlist(thelist, names=None):
    for nvitem in thelist:
        if isinstance(nvitem, dict):
            name, value = next(six.iteritems(nvitem))
            if names is None or name in names:
                yield nvitem, name, value