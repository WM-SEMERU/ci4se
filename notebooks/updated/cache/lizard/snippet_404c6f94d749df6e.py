def auto_override_module(md, force_recursive=False):
    if not pytypes.checking_enabled:
        return md
    if isinstance(md, str):
        if md in sys.modules:
            md = sys.modules[md]
            if md is None:
                return md
        elif md in _pending_modules:
            _pending_modules[md].append(lambda t: auto_override_module(t, True)
                )
            return md
    assert ismodule(md)
    if md.__name__ in _pending_modules:
        _pending_modules[md.__name__].append(lambda t: auto_override_module
            (t, True))
    if md.__name__ in _auto_override_modules and _auto_override_modules[md.
        __name__] == len(md.__dict__):
        return md
    keys = [key for key in md.__dict__]
    for key in keys:
        memb = md.__dict__[key]
        if force_recursive or not is_no_type_check(memb):
            if isclass(memb) and memb.__module__ == md.__name__:
                auto_override_class(memb, force_recursive, force_recursive)
    if not md.__name__ in _pending_modules:
        _auto_override_modules[md.__name__] = len(md.__dict__)
    return md