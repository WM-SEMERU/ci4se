def get_fn_args(fn, kwargs: dict, prefix: str=None):
    all_args = get_all_args(fn)
    required_args = get_required_args(fn)
    fn_kwargs = pick_kwargs(kwargs, all_args, prefix)
    missing_args = [arg for arg in required_args if arg not in fn_kwargs]
    if missing_args:
        raise ValueError(
            'The following args are missing for the function {}: {}.'.
            format(fn.__name__, missing_args))
    return fn_kwargs