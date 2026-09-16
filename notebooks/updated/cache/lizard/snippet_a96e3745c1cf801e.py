def _subgroup(group, *args, **kwargs):

    def decorator(f):
        f.required = kwargs.pop('required', True)
        if 'parents' in kwargs:
            if not hasattr(f, '_argnames'):
                f._argnames = []
            for p in kwargs['parents']:
                f._argnames += p._argnames if hasattr(p, '_argnames') else []
            kwargs['parents'] = [p.parser for p in kwargs['parents']]
        if 'help' not in kwargs:
            kwargs['help'] = f.__doc__
        if args == ():
            f.parser = group._subparsers.add_parser(f.__name__, **kwargs)
        else:
            f.parser = group._subparsers.add_parser(*args, **kwargs)
        f.parser.set_defaults(**{('_func_' + group.__name__): f})
        f.climax = True
        for arg in getattr(f, '_arguments', []):
            f.parser.add_argument(*arg[0], **arg[1])
        f._subparsers = f.parser.add_subparsers()
        f.command = partial(_subcommand, f)
        f.group = partial(_subgroup, f)
        return f
    return decorator