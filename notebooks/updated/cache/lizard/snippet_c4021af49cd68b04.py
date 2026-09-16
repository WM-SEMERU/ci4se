def _get_remote_method(self, funcname):
    func = getattr(self, funcname)
    if not callable(func) or not getattr(func, '_remote', False):
        raise AttributeError('%r object has no attribute %r' % (self.
            __class__.__name__, funcname))
    return func