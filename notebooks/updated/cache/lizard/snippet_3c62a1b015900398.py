def asyncPipeStrconcat(context=None, _INPUT=None, conf=None, **kwargs):
    splits = yield asyncGetSplits(_INPUT, conf['part'], **cdicts(opts, kwargs))
    _OUTPUT = yield asyncStarMap(partial(maybeDeferred, parse_result), splits)
    returnValue(iter(_OUTPUT))