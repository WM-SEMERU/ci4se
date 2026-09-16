def set_ordered(self, value, inplace=False):
    inplace = validate_bool_kwarg(inplace, 'inplace')
    new_dtype = CategoricalDtype(self.categories, ordered=value)
    cat = self if inplace else self.copy()
    cat._dtype = new_dtype
    if not inplace:
        return cat