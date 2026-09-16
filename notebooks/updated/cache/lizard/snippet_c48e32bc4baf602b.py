def search(self, index, query, **kwargs):
    itercls = kwargs.pop('itercls', _FTS.SearchRequest)
    iterargs = itercls.mk_kwargs(kwargs)
    params = kwargs.pop('params', _FTS.Params(**kwargs))
    body = _FTS.make_search_body(index, query, params)
    return itercls(body, self, **iterargs)