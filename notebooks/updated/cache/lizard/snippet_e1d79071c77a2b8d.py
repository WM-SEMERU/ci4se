def normalizeInternalObjectType(value, cls, name):
    if not isinstance(value, cls):
        raise TypeError('%s must be a %s instance, not %s.' % (name, name,
            type(value).__name__))
    return value