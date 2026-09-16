def mkRepr(instance, *argls, **kwargs):
    r
    width = 79
    maxIndent = 15
    minIndent = 2
    args = map(repr, argls) + [('%s=%r' % (k, v)) for k, v in sorted(kwargs
        .items())] or ['']
    if instance is not None:
        start = '%s(' % instance.__class__.__name__
        args[-1] += ')'
    else:
        start = ''
    if len(start) <= maxIndent and len(start) + len(args[0]) <= width and max(
        map(len, args)) <= width:
        indent = len(start)
        args[0] = start + args[0]
        if sum(map(len, args)) + 2 * (len(args) - 1) <= width:
            return ', '.join(args)
    else:
        indent = minIndent
        args[0] = start + '\n' + ' ' * indent + args[0]
    return (',\n' + ' ' * indent).join(args)