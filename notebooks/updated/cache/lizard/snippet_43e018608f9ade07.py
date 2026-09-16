def init_app(self, app):
    if self.module:
        app.config.from_object(self.module)