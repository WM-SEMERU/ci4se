def check_status(status, expected, path, headers=None, resp_headers=None,
    body=None, extras=None):
    if status in expected:
        return
    msg = (
        """Expect status %r from Google Storage. But got status %d.
Path: %r.
Request headers: %r.
Response headers: %r.
Body: %r.
Extra info: %r.
"""
         % (expected, status, path, headers, resp_headers, body, extras))
    if status == httplib.UNAUTHORIZED:
        raise AuthorizationError(msg)
    elif status == httplib.FORBIDDEN:
        raise ForbiddenError(msg)
    elif status == httplib.NOT_FOUND:
        raise NotFoundError(msg)
    elif status == httplib.REQUEST_TIMEOUT:
        raise TimeoutError(msg)
    elif status == httplib.REQUESTED_RANGE_NOT_SATISFIABLE:
        raise InvalidRange(msg)
    elif status == httplib.OK and 308 in expected and httplib.OK not in expected:
        raise FileClosedError(msg)
    elif status >= 500:
        raise ServerError(msg)
    else:
        raise FatalError(msg)