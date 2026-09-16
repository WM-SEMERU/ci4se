def apply_(name, mods=None, **kwargs):
    if mods:
        return sls(name, mods, **kwargs)
    return highstate(name, **kwargs)