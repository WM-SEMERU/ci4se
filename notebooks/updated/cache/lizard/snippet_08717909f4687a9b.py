def _writer(func):
    name = func.__name__
    return property(fget=lambda self: getattr(self, '_%s' % name), fset=func)