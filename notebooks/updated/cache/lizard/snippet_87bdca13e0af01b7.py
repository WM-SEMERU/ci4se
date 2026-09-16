def jsonhash(obj, root=True, exclude=None, hash_func=_jsonhash_sha1):
    if isinstance(obj, Mapping):
        if root and exclude:
            obj = {k: v for k, v in obj.iteritems() if k not in exclude}
        result = sorted((k, jsonhash(v, False)) for k, v in obj.iteritems())
    elif isinstance(obj, list):
        result = tuple(jsonhash(e, False) for e in obj)
    else:
        result = obj
    if root:
        result = unicode(hash_func(result))
    return result