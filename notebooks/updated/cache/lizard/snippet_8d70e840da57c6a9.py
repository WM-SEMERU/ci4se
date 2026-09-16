def _parse(args):
    ordered = []
    opt_full = dict()
    opt_abbrev = dict()
    args = args + ['']
    i = 0
    while i < len(args) - 1:
        arg = args[i]
        arg_next = args[i + 1]
        if arg.startswith('--'):
            if arg_next.startswith('-'):
                raise ValueError('{} lacks value'.format(arg))
            else:
                opt_full[arg[2:]] = arg_next
                i += 2
        elif arg.startswith('-'):
            if arg_next.startswith('-'):
                raise ValueError('{} lacks value'.format(arg))
            else:
                opt_abbrev[arg[1:]] = arg_next
                i += 2
        else:
            ordered.append(arg)
            i += 1
    return ordered, opt_full, opt_abbrev