def coerce_value(cls, v):
    if isinstance(v, cls.itemtype):
        return v
    else:
        try:
            return cls.coerceitem(v)
        except Exception as e:
            raise exc.CollectionItemCoerceError(itemtype=cls.itemtype,
                colltype=cls, passed=v, exc=e)