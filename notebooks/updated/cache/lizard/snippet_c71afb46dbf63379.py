def hasApplication(self, app):
    if self._applications is None:
        self._initApplicationList()
    return app in self._applications