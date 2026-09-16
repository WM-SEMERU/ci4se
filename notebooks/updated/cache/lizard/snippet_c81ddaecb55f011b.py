def fallback_findfile(filename):
    mods = [m for m in sys.modules.values() if m and hasattr(m, '__file__') and
        filename in m.__file__]
    if len(mods) == 0:
        return None
    alt_fn = mods[0].__file__
    if alt_fn[-4:-1] == '.py':
        alt_fn = alt_fn[:-1]
    if not os.path.exists(alt_fn) and alt_fn.startswith('./'):
        alt_fn2 = _cur_pwd + alt_fn[1:]
        if os.path.exists(alt_fn2):
            return alt_fn2
        for m in ['__main__', 'better_exchook']:
            if hasattr(sys.modules.get(m), '__file__'):
                alt_fn2 = os.path.dirname(sys.modules[m].__file__) + alt_fn[1:]
                if os.path.exists(alt_fn2):
                    return alt_fn2
    return alt_fn