def init_app(self, app, **kwargs):
    self.kwargs.update(kwargs)
    self.settings = self.dynaconf_instance or LazySettings(**self.kwargs)
    app.config = self.make_config(app)
    app.dynaconf = self.settings