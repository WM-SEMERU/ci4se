def wrap_constant(self, val):
    from .queries import QueryBuilder
    if isinstance(val, (Term, QueryBuilder, Interval)):
        return val
    if val is None:
        return NullValue()
    if isinstance(val, list):
        return Array(*val)
    if isinstance(val, tuple):
        return Tuple(*val)
    _ValueWrapper = getattr(self, '_wrapper_cls', ValueWrapper)
    return _ValueWrapper(val)