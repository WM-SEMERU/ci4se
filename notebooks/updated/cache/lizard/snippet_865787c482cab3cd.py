def _unicode_handler(obj):
    try:
        result = obj.isoformat()
    except AttributeError:
        raise TypeError('Unserializable object {} of type {}'.format(obj,
            type(obj)))
    return result