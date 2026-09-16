def orderby(cls, ops, kwargs):
    return sorted(ops, key=cls.order_key), kwargs