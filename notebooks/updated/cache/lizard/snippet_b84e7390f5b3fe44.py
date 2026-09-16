def del_method(self, m):
    if isinstance(m, types.FunctionType) and not iscoroutinefunction(m):
        wrkey = 'function', id(m)
    else:
        f, obj = get_method_vars(m)
        wrkey = f, id(obj)
    if wrkey in self:
        del self[wrkey]