def type_name(self):
    res = self.type.__name__
    if self.type.__module__ not in ('__builtin__', 'builtins'):
        res = self.type.__module__ + '.' + res
    return res