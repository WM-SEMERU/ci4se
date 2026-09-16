def args_to_int(mapping, argument):
    if isinstance(argument, int):
        if argument == 0:
            return 0
        deprecation('passing extensions and flags as constants is deprecated')
        return argument
    elif isinstance(argument, (tuple, list)):
        return reduce(op.or_, [mapping[n] for n in set(argument) if n in
            mapping], 0)
    raise TypeError('argument must be a list of strings or an int')