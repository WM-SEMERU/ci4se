def wsgi_wrap(app):

    @wraps(app)
    def wrapped(environ, start_response):
        status_headers = [None, None]

        def _start_response(status, headers):
            status_headers[:] = [status, headers]
        body = app(environ, _start_response)
        ret = body, status_headers[0], status_headers[1]
        return ret
    return wrapped