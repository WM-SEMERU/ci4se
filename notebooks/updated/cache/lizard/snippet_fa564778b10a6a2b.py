def _construct_register(reg, default_reg):
    if reg:
        x = dict((k, reg.get(k, d)) for k, d in default_reg.items())
    else:
        x = dict(default_reg)
    return x