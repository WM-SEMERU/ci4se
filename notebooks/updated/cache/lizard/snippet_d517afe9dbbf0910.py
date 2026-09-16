def coerce_types(T1, T2):
    if T1 is T2:
        return T1
    if T1 is int:
        return T2
    if T2 is int:
        return T1
    if issubclass(T2, T1):
        return T2
    if issubclass(T1, T2):
        return T1
    if issubclass(T2, float):
        return T2
    if issubclass(T1, float):
        return T1
    if T1.__base__ is T2.__base__:
        return T2
    raise TypeError('cannot coerce types %r and %r' % (T1, T2))