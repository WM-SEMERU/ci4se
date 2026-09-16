def allow_origins(self, *origins, methods=None, max_age=None, credentials=
    None, headers=None, **overrides):
    response_headers = {}
    if origins:

        @hug.response_middleware()
        def process_data(request, response, resource):
            if 'ORIGIN' in request.headers:
                origin = request.headers['ORIGIN']
                if origin in origins:
                    response.set_header('Access-Control-Allow-Origin', origin)
    else:
        response_headers['Access-Control-Allow-Origin'] = '*'
    if methods:
        response_headers['Access-Control-Allow-Methods'] = ', '.join(methods)
    if max_age:
        response_headers['Access-Control-Max-Age'] = max_age
    if credentials:
        response_headers['Access-Control-Allow-Credentials'] = str(credentials
            ).lower()
    if headers:
        response_headers['Access-Control-Allow-Headers'] = headers
    return self.add_response_headers(response_headers, **overrides)