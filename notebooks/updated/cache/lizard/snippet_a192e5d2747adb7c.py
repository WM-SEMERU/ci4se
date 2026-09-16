def replace_refs(cls, obj, _recursive=False, **kwargs):
    store = kwargs.setdefault('_store', _URIDict())
    base_uri, frag = urlparse.urldefrag(kwargs.get('base_uri', ''))
    store_uri = None
    if not frag and not _recursive:
        store_uri = base_uri
    try:
        if kwargs.get('jsonschema') and isinstance(obj['id'], basestring):
            kwargs['base_uri'] = urlparse.urljoin(kwargs.get('base_uri', ''
                ), obj['id'])
            store_uri = kwargs['base_uri']
    except (TypeError, LookupError):
        pass
    try:
        if not isinstance(obj['$ref'], basestring):
            raise TypeError
    except (TypeError, LookupError):
        pass
    else:
        return cls(obj, **kwargs)
    kwargs['_recursive'] = True
    path = list(kwargs.pop('_path', ()))
    if isinstance(obj, Mapping):
        obj = type(obj)((k, cls.replace_refs(v, _path=path + [k], **kwargs)
            ) for k, v in iteritems(obj))
    elif isinstance(obj, Sequence) and not isinstance(obj, basestring):
        obj = type(obj)(cls.replace_refs(v, _path=path + [i], **kwargs) for
            i, v in enumerate(obj))
    if store_uri is not None:
        store[store_uri] = obj
    return obj