def resolve_url_ext(to, params_=None, anchor_=None, args=None, kwargs=None):
    url = resolve_url(to, *(args or ()), **kwargs or {})
    if params_:
        url += '?' + urllib.urlencode(encode_url_query_params(params_))
    if anchor_:
        url += '#' + anchor_
    return url