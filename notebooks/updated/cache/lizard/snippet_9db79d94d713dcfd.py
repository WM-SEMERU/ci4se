def TextInfo(filename=None, editable=False, **kwargs):
    args = []
    if filename:
        args.append('--filename=%s' % filename)
    if editable:
        args.append('--editable')
    for generic_args in kwargs_helper(kwargs):
        args.append('--%s=%s' % generic_args)
    p = run_zenity('--text-info', *args)
    if p.wait() == 0:
        return p.stdout.read()