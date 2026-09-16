def _models(self, appname):
    try:
        app = self._get_app(appname)
    except Exception as e:
        self.err('Can not get app ' + appname, e)
        return
    if appname not in self.appnames:
        self.err('App ' + appname + ' not found in settings')
        return
    models = self._get_models(app)
    return models