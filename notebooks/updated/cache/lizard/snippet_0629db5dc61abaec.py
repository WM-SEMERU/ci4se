def extend_args(function_signature, args, kwargs):
    arg_names = function_signature.arg_names
    arg_defaults = function_signature.arg_defaults
    arg_is_positionals = function_signature.arg_is_positionals
    keyword_names = function_signature.keyword_names
    function_name = function_signature.function_name
    args = list(args)
    for keyword_name in kwargs:
        if keyword_name not in keyword_names:
            raise Exception(
                "The name '{}' is not a valid keyword argument for the function '{}'."
                .format(keyword_name, function_name))
    for skipped_name in arg_names[0:len(args)]:
        if skipped_name in kwargs:
            raise Exception(
                "Positional and keyword value provided for the argument '{}' for the function '{}'"
                .format(keyword_name, function_name))
    zipped_info = zip(arg_names, arg_defaults, arg_is_positionals)
    zipped_info = list(zipped_info)[len(args):]
    for keyword_name, default_value, is_positional in zipped_info:
        if keyword_name in kwargs:
            args.append(kwargs[keyword_name])
        elif default_value != funcsigs._empty:
            args.append(default_value)
        elif not is_positional:
            raise Exception(
                "No value was provided for the argument '{}' for the function '{}'."
                .format(keyword_name, function_name))
    no_positionals = len(arg_is_positionals) == 0 or not arg_is_positionals[-1]
    too_many_arguments = len(args) > len(arg_names) and no_positionals
    if too_many_arguments:
        raise Exception("Too many arguments were passed to the function '{}'"
            .format(function_name))
    return args