def mapkeys(function, dict_):
    ensure_mapping(dict_)
    function = identity() if function is None else ensure_callable(function)
    return dict_.__class__((function(k), v) for k, v in iteritems(dict_))