def get(cls, id=None, condition=None, fields=None, cache=False, engine_name
    =None, **kwargs):
    if id is None and condition is None:
        return None
    can_cacheable = (cache or getattr(cls, '__cacheable__', None)
        ) and isinstance(id, (int, long, str, unicode))
    if can_cacheable:
        obj = dispatch.get(cls, 'get_object', id)
        if obj:
            return obj
    if condition is not None:
        _cond = condition
    elif is_condition(id):
        _cond = id
    else:
        _cond = cls.c[cls._primary_field] == id
    obj = cls.filter(_cond, **kwargs).fields(*(fields or [])).one()
    if obj and cache or getattr(cls, '__cacheable__', None):
        dispatch.call(cls, 'set_object', instance=obj)
    return obj