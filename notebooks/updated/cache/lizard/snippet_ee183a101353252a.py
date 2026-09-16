def init_app(self, app):
    app.config.from_pyfile('{0}.cfg'.format(app.name), silent=True)