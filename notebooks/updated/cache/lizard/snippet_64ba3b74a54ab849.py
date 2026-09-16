def adapt(obj, to_cls):
    if obj is None:
        return obj
    elif isinstance(obj, to_cls):
        return obj
    errors = []
    if hasattr(obj, '__adapt__') and obj.__adapt__:
        try:
            return obj.__adapt__(to_cls)
        except (AdaptError, TypeError) as e:
            ex_type, ex, tb = sys.exc_info()
            errors.append((obj.__adapt__, ex_type, ex, tb))
    if hasattr(to_cls, '__adapt__') and to_cls.__adapt__:
        try:
            return to_cls.__adapt__(obj)
        except (AdaptError, TypeError) as e:
            ex_type, ex, tb = sys.exc_info()
            errors.append((to_cls.__adapt__, ex_type, ex, tb))
    for k in get_adapter_path(obj, to_cls):
        if k in __adapters__:
            try:
                return __adapters__[k](obj, to_cls)
            except (AdaptError, TypeError) as e:
                ex_type, ex, tb = sys.exc_info()
                errors.append((__adapters__[k], ex_type, ex, tb))
                break
    raise AdaptErrors('Could not adapt %r to %r' % (obj, to_cls), errors=errors
        )