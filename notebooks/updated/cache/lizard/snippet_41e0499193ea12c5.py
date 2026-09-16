def from_httplib(ResponseCls, r, **response_kw):
    headers = r.msg
    if not isinstance(headers, HTTPHeaderDict):
        if PY3:
            headers = HTTPHeaderDict(headers.items())
        else:
            headers = HTTPHeaderDict.from_httplib(headers)
    strict = getattr(r, 'strict', 0)
    resp = ResponseCls(body=r, headers=headers, status=r.status, version=r.
        version, reason=r.reason, strict=strict, original_response=r, **
        response_kw)
    return resp