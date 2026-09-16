def identify_module(arg):
    try:
        __import__(arg)
    except Exception:
        exc = sys.exc_info()[1]
        raise ModuleNotFound('%s: %s' % (type(exc).__name__, str(exc)))
    mod = sys.modules[arg]
    return mod