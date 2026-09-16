def _handle_headers(self):
    origin = self.request.headers.get('Origin')
    if not settings.DEBUG:
        if origin in settings.ALLOWED_ORIGINS or not origin:
            self.set_header('Access-Control-Allow-Origin', origin)
        else:
            log.debug('CORS ERROR: %s not allowed, allowed hosts: %s' % (
                origin, settings.ALLOWED_ORIGINS))
            raise HTTPError(403, 'Origin not in ALLOWED_ORIGINS: %s' % origin)
    else:
        self.set_header('Access-Control-Allow-Origin', origin or '*')
    self.set_header('Access-Control-Allow-Credentials', 'true')
    self.set_header('Access-Control-Allow-Headers', 'Content-Type')
    self.set_header('Access-Control-Allow-Methods', 'OPTIONS')
    self.set_header('Content-Type', 'application/json')