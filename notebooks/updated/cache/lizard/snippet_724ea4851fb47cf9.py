def add_response_headers(headers):

    def decorator(func):

        @wraps(func)
        def _(*args, **kwargs):
            rsp = make_response(func(*args, **kwargs))
            rsp_headers = rsp.headers
            for header, value in headers.items():
                rsp_headers[header] = value
            return rsp
        return _
    return decorator