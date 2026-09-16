def unpack(rv):
    if isinstance(rv, ResponseBase):
        return rv
    status = headers = None
    if isinstance(rv, tuple):
        rv, status, headers = rv + (None,) * (3 - len(rv))
    if rv is None:
        raise ValueError('View function did not return a response')
    if status is None:
        status = 200
    return rv, status, headers or {}