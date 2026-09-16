def import_name(stref: str):
    h = stref
    p = []
    m = None
    try:
        r = importlib.util.find_spec(stref)
    except (AttributeError, ImportError):
        r = None
    if r is not None:
        return importlib.import_module(stref)
    while '.' in h:
        h, t = h.rsplit('.', 1)
        p.append(t)
        if h in sys.modules:
            m = sys.modules[h]
            break
    if m is None:
        m = importlib.import_module(h)
    for i in reversed(p):
        if hasattr(m, i):
            m = getattr(m, i)
        else:
            h += '.' + i
            m = importlib.import_module(h)
    logger.debug('Imported "%s" as %r', stref, m)
    return m