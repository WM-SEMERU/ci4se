def _set_options_headers(self, methods):
    request = self.request
    response = request.response
    response.headers['Allow'] = ', '.join(sorted(methods))
    if 'Access-Control-Request-Method' in request.headers:
        response.headers['Access-Control-Allow-Methods'] = ', '.join(sorted
            (methods))
    if 'Access-Control-Request-Headers' in request.headers:
        response.headers['Access-Control-Allow-Headers'
            ] = 'origin, x-requested-with, content-type'
    return response