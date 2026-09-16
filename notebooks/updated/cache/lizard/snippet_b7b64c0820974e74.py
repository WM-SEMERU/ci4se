def asyncPipeRename(context=None, _INPUT=None, conf=None, **kwargs):
    splits = yield asyncGetSplits(_INPUT, conf['RULE'], **cdicts(opts, kwargs))
    _OUTPUT = yield maybeDeferred(parse_results, splits, **kwargs)
    returnValue(_OUTPUT)