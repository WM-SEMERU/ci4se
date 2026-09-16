def bddvar(name, index=None):
    r
    bvar = boolfunc.var(name, index)
    try:
        var = _VARS[bvar.uniqid]
    except KeyError:
        var = _VARS[bvar.uniqid] = BDDVariable(bvar)
        _BDDS[var.node] = var
    return var