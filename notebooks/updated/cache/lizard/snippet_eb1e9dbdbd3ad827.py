def async_fetch(request, method, default_headers=None, callback=None,
    httpclient=None, **kwargs):
    updated_request = make_request(request, method, default_headers, **kwargs)
    if not httpclient:
        httpclient = AsyncHTTPClient()
    rsp = yield httpclient.fetch(updated_request)
    raise Return(parse_response(rsp))