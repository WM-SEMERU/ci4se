def fn_kwargs(callable):
    fn = get_fn(callable)
    args, _, _, defaults = _inspect.getargspec(fn)
    if defaults is None:
        return {}
    return dict(list(zip(reversed(args), reversed(defaults))))