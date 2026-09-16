def init_app(self, app):
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    app.extensions['flask-graphql-auth'] = self
    self._set_default__configuration_options(app)