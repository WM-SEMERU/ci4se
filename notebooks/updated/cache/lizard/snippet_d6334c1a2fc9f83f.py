def get_value(self, obj, attr, accessor=None, default=missing_):
    attribute = getattr(self, 'attribute', None)
    accessor_func = accessor or utils.get_value
    check_key = attr if attribute is None else attribute
    return accessor_func(obj, check_key, default)