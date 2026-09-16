def scalar_input_map(func, input_):
    if util_iter.isiterable(input_):
        return list(map(func, input_))
    else:
        return func(input_)