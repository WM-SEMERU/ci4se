def as_ordered(self, inplace=False):
    inplace = validate_bool_kwarg(inplace, 'inplace')
    return self.set_ordered(True, inplace=inplace)