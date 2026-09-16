def apply_dict_default(dictionary, arg, default):
    if arg not in dictionary:
        if hasattr(default, '__call__'):
            default = restrict_args(default, arg)
        dictionary[arg] = default
    return dictionary