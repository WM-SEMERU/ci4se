def eglQueryString(display, name):
    out = _lib.eglQueryString(display, name)
    if not out:
        raise RuntimeError('Could not query %s' % name)
    return out