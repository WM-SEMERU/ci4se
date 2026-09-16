def process_response(self, request, response, resource):
    origin = request.get_header('Origin')
    if not settings.DEBUG:
        if origin in settings.ALLOWED_ORIGINS or not origin:
            response.set_header('Access-Control-Allow-Origin', origin)
        else:
            log.debug('CORS ERROR: %s not allowed, allowed hosts: %s' % (
                origin, settings.ALLOWED_ORIGINS))
            raise falcon.HTTPForbidden('Denied', 
                'Origin not in ALLOWED_ORIGINS: %s' % origin)
    else:
        response.set_header('Access-Control-Allow-Origin', origin or '*')
    response.set_header('Access-Control-Allow-Credentials', 'true')
    response.set_header('Access-Control-Allow-Headers', 'Content-Type')
    response.set_header('Access-Control-Allow-Methods', 'OPTIONS')