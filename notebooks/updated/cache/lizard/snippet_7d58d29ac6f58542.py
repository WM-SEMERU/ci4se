def isqref(object):
    return isinstance(object, tuple) and len(object) == 2 and isinstance(object
        [0], basestring) and isinstance(object[1], basestring)