def recursive_unicode(obj):
    if isinstance(obj, dict):
        return dict((recursive_unicode(k), recursive_unicode(v)) for k, v in
            obj.items())
    elif isinstance(obj, list):
        return list(recursive_unicode(i) for i in obj)
    elif isinstance(obj, tuple):
        return tuple(recursive_unicode(i) for i in obj)
    elif isinstance(obj, bytes_type):
        return to_unicode(obj)
    else:
        return obj