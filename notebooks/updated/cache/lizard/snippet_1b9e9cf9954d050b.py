def init_app(self, app):
    self.app = app
    self._session_conf = app.config.get('BEAKER_SESSION', {'session.type':
        'file', 'session.data_dir': '/tmp/session/data', 'session.lock_dir':
        '/tmp/session/lock'})
    app.wsgi_app = SessionMiddleware(app.wsgi_app, self._session_conf)
    app.session_interface = BeakerSessionInterface()