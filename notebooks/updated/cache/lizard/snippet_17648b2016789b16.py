def deprecated_opts_signature(args, kwargs):
    from .options import Options
    groups = set(Options._option_groups)
    opts = {kw for kw in kwargs if kw != 'clone'}
    apply_groups = False
    options = None
    new_kwargs = {}
    if len(args) > 0 and isinstance(args[0], dict):
        apply_groups = True
        if not set(args[0]).issubset(groups) and all(isinstance(v, dict) and
            not set(v).issubset(groups) for v in args[0].values()):
            apply_groups = False
        elif set(args[0].keys()) <= groups:
            new_kwargs = args[0]
        else:
            options = args[0]
    elif opts and opts.issubset(set(groups)):
        apply_groups = True
    elif kwargs.get('options', None) is not None:
        apply_groups = True
    elif not args and not kwargs:
        apply_groups = True
    return apply_groups, options, new_kwargs