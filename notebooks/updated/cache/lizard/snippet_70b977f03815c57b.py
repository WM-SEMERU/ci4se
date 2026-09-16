def _asdict_anything(val, filter, dict_factory, retain_collection_types):
    if getattr(val.__class__, '__attrs_attrs__', None) is not None:
        rv = asdict(val, True, filter, dict_factory, retain_collection_types)
    elif isinstance(val, (tuple, list, set)):
        cf = val.__class__ if retain_collection_types is True else list
        rv = cf([_asdict_anything(i, filter, dict_factory,
            retain_collection_types) for i in val])
    elif isinstance(val, dict):
        df = dict_factory
        rv = df((_asdict_anything(kk, filter, df, retain_collection_types),
            _asdict_anything(vv, filter, df, retain_collection_types)) for 
            kk, vv in iteritems(val))
    else:
        rv = val
    return rv