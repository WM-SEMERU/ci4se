def check_conditions(f, args, kwargs):
    member_function = is_member_function(f)
    check_preconditions(f, args, kwargs)
    base_classes = []
    if member_function:
        base_classes = inspect.getmro(type(args[0]))[1:-1]
        for clz in base_classes:
            super_fn = getattr(clz, f.func_name, None)
            check_preconditions(super_fn, args, kwargs)
    return_value = f(*args, **kwargs)
    check_postconditions(f, return_value)
    if member_function:
        for clz in base_classes:
            super_fn = getattr(clz, f.func_name, None)
            check_postconditions(super_fn, return_value)
    return return_value