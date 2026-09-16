def installed(self, app=None):
    if app is None:
        app = current_app
    return self.__EXTENSION_NAME in app.extensions