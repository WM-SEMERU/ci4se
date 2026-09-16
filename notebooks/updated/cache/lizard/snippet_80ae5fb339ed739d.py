def rerender_options(options):
    args = []
    for name, value in options.iteritems():
        name = name.replace('_', '-')
        if value is None:
            pass
        elif isinstance(value, bool):
            if value:
                args.append('--%s' % (name,))
        elif isinstance(value, list):
            for item in value:
                args.append('--%s=%s' % (name, item))
        else:
            args.append('--%s=%s' % (name, value))
    return ' '.join(args)