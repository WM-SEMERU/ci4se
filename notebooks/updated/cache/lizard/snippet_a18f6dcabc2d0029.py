def _translate(env, target=None, source=SCons.Environment._null, *args, **kw):
    if target is None:
        target = []
    pot = env.POTUpdate(None, source, *args, **kw)
    po = env.POUpdate(target, pot, *args, **kw)
    return po