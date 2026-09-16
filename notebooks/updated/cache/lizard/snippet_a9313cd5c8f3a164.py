def build_dummy_request(newsitem):
    url = newsitem.full_url
    if url:
        url_info = urlparse(url)
        hostname = url_info.hostname
        path = url_info.path
        port = url_info.port or 80
    else:
        try:
            hostname = settings.ALLOWED_HOSTS[0]
        except IndexError:
            hostname = 'localhost'
        path = '/'
        port = 80
    request = WSGIRequest({'REQUEST_METHOD': 'GET', 'PATH_INFO': path,
        'SERVER_NAME': hostname, 'SERVER_PORT': port, 'HTTP_HOST': hostname,
        'wsgi.input': StringIO()})
    handler = BaseHandler()
    handler.load_middleware()
    if hasattr(handler, '_request_middleware'):
        for middleware_method in handler._request_middleware:
            middleware_method(request)
    else:
        handler.get_response(request)
    return request