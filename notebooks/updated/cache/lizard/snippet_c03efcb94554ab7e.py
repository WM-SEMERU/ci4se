def apply(self, func, keep_attrs=None, args=(), **kwargs):
    variables = OrderedDict((k, maybe_wrap_array(v, func(v, *args, **kwargs
        ))) for k, v in self.data_vars.items())
    if keep_attrs is None:
        keep_attrs = _get_keep_attrs(default=False)
    attrs = self.attrs if keep_attrs else None
    return type(self)(variables, attrs=attrs)