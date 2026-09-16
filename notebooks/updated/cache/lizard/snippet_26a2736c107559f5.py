def required_arguments(func):
    defaults = default_values_of(func)
    args = arguments_of(func)
    if defaults:
        args = args[:-len(defaults)]
    return args