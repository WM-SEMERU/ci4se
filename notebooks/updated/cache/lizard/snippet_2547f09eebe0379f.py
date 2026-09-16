def set_attrs(obj, attrs):
    o = setattr
    if hasattr(obj, '__setitem__'):
        o = type(obj).__setitem__
    [o(obj, k, v) for k, v in attrs.iteritems()]