def starfilteritems(predicate, dict_):
    ensure_mapping(dict_)
    if predicate is None:
        predicate = lambda k, v: all((k, v))
    else:
        ensure_callable(predicate)
    return dict_.__class__((k, v) for k, v in iteritems(dict_) if predicate
        (k, v))