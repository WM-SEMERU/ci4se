def pretty_format_args(*args, **kwargs):
    args = list([repr(a) for a in args])
    for key, value in kwargs.items():
        args.append('%s=%s' % (key, repr(value)))
    return '(%s)' % ', '.join([a for a in args])