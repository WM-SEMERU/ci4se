def _start_server(self, *args):
    self.log('Starting server', args)
    secure = self.certificate is not None
    if secure:
        self.log('Running SSL server with cert:', self.certificate)
    else:
        self.log(
            'Running insecure server without SSL. Do not use without SSL proxy in production!'
            , lvl=warn)
    try:
        self.server = Server((self.host, self.port), secure=secure,
            certfile=self.certificate).register(self)
    except PermissionError:
        self.log('Could not open (privileged?) port, check permissions!',
            lvl=critical)