def incr_obj(obj, **attrs):
    for name, value in attrs.iteritems():
        v = getattr(obj, name, None)
        if not hasattr(obj, name) or v is None:
            v = 0
        setattr(obj, name, v + value)