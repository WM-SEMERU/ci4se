def is_wrapped_arg(self, *args, **kwargs):
    ret = False
    if len(args) == 1 and len(kwargs) == 0:
        ret = inspect.isfunction(args[0]) or isinstance(args[0], type
            ) or isinstance(args[0], Decorator)
        if ret:
            ret = not self.required_args
    return ret