def callable_check(func, arg_count=1, arg_value=None, allow_none=False):
    if func is None:
        if not allow_none:
            raise ValueError('callable cannot be None')
    elif not arg_checker(func, *[arg_value for _ in range(arg_count)]):
        raise ValueError('callable %s invalid (for %d arguments)' % (func,
            arg_count))