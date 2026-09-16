def _setdef(argdict, name, defaultvalue):
    if not name in argdict or argdict[name] is None:
        argdict[name] = defaultvalue
    return argdict[name]