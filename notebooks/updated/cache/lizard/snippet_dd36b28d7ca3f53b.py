def _int_antsProcessArguments(args):
    p_args = []
    if isinstance(args, dict):
        for argname, argval in args.items():
            if '-MULTINAME-' in argname:
                argname = argname[:argname.find('-MULTINAME-')]
            if argval is not None:
                if len(argname) > 1:
                    p_args.append('--%s' % argname)
                else:
                    p_args.append('-%s' % argname)
                if isinstance(argval, iio.ANTsImage):
                    p_args.append(_ptrstr(argval.pointer))
                elif isinstance(argval, list):
                    for av in argval:
                        if isinstance(av, iio.ANTsImage):
                            av = _ptrstr(av.pointer)
                        p_args.append(av)
                else:
                    p_args.append(str(argval))
    elif isinstance(args, list):
        for arg in args:
            if isinstance(arg, iio.ANTsImage):
                pointer_string = _ptrstr(arg.pointer)
                p_arg = pointer_string
            elif arg is None:
                pass
            else:
                p_arg = str(arg)
            p_args.append(p_arg)
    return p_args