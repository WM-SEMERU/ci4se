def register_all_shape_checker(shape_checker_function, arg_types, exclude=(
    ), ignore_existing=False):
    for t1 in arg_types:
        for t2 in arg_types:
            if (t1, t2) in exclude:
                continue
            if ignore_existing and (t1, t2) in shape_checkers:
                continue
            register_shape_checker(t1, t2, shape_checker_function)