def get_class_qualname(cls):
    if hasattr(cls, '__qualname__'):
        return cls.__qualname__
    module = sys.modules[cls.__module__]
    if cls.__module__ == 'typing' and not hasattr(cls, '__name__'):
        return cls._name
    if hasattr(module, cls.__name__) and getattr(module, cls.__name__) is cls:
        return cls.__name__
    else:
        nst = _get_class_nesting_list(cls, module)
        nst.append(cls)
        nst = [cl.__name__ for cl in nst]
        return '.'.join(nst)
    return cls.__name__