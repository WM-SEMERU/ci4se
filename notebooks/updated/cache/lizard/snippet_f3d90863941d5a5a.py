def init_app(self, app):
    state = self.init_mail(app.config, app.debug, app.testing)
    app.extensions = getattr(app, 'extensions', {})
    app.extensions['mail'] = state
    return state