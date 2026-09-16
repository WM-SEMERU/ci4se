def init_app(self, app):
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    app.extensions['flask-jwt-simple'] = self
    self._set_default_configuration_options(app)
    self._set_error_handler_callbacks(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True