def merge_options(cls, groups, options=None, **kwargs):
    groups = set(groups)
    if options is not None and set(options.keys()) <= groups:
        kwargs, options = options, None
    elif options is not None and any(k in groups for k in options):
        raise Exception('All keys must be a subset of %s' % ', '.join(groups))
    options = {} if options is None else dict(**options)
    all_keys = set(k for d in kwargs.values() for k in d)
    for spec_key in all_keys:
        additions = {}
        for k, d in kwargs.items():
            if spec_key in d:
                kws = d[spec_key]
                additions.update({k: kws})
        if spec_key not in options:
            options[spec_key] = {}
        for key in additions:
            if key in options[spec_key]:
                options[spec_key][key].update(additions[key])
            else:
                options[spec_key][key] = additions[key]
    return options