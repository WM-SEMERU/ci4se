def _derive_typedef(typ):
    v = [v for v in _values(_typedefs) if _issubclass(typ, v.type)]
    if len(v) == 1:
        return v[0]
    return None