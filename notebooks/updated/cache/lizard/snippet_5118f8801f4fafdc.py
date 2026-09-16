def app(environ, start_response):
    try:
        if environ['REQUEST_METHOD'] == 'GET':
            start_response('200 OK', [('content-type', 'text/html')])
            return ['Hellow world!']
        else:
            start_response('405 Method Not Allowed', [('content-type',
                'text/html')])
            return ['']
    except Exception as ex:
        start_response('500 Internal Server Error', [('content-type',
            'text/html')], sys.exc_info())
        return _handle_exc(ex)