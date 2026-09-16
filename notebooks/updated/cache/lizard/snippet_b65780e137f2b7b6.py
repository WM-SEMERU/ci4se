def get_request_mock():
    basehandler = BaseHandler()
    basehandler.load_middleware()
    request = WSGIRequest({'HTTP_COOKIE': '', 'PATH_INFO': '/',
        'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'REQUEST_METHOD':
        'GET', 'SERVER_NAME': 'page-request-mock', 'SCRIPT_NAME': '',
        'SERVER_PORT': '80', 'SERVER_PROTOCOL': 'HTTP/1.1', 'HTTP_HOST':
        'page-request-host', 'CONTENT_TYPE': 'text/html; charset=utf-8',
        'wsgi.version': (1, 0), 'wsgi.url_scheme': 'http',
        'wsgi.multiprocess': True, 'wsgi.multithread': False,
        'wsgi.run_once': False, 'wsgi.input': StringIO()})
    for middleware_method in basehandler._request_middleware:
        if 'LocaleMiddleware' not in str(middleware_method.__class__):
            middleware_method(request)
    return request