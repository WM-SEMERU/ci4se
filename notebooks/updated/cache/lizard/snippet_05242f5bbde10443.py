def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    if request_body_size > 0:
        request_body = environ['wsgi.input'].read(request_body_size)
    else:
        request_body = environ['wsgi.input'].read()
    form = cgi.parse_qs(request_body)
    status = '200 OK'
    start_response(status, get_response_headers())
    for output in checklink(form=form, env=environ):
        yield output