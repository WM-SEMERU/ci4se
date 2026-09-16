def value_attr(attr_name):

    def value_attr(value, context, **_params):
        value = getattr(value, attr_name)
        return _attr(value)
    return value_attr