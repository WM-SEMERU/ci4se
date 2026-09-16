def pipe_rename(context=None, _INPUT=None, conf=None, **kwargs):
    splits = get_splits(_INPUT, conf['RULE'], **cdicts(opts, kwargs))
    _OUTPUT = parse_results(splits, **kwargs)
    return _OUTPUT