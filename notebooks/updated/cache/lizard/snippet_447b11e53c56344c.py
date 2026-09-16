def saveProfile(self, key, settings=None):
    if settings is None:
        settings = QtCore.QSettings()
    settings.setValue(key, self.horizontalHeader().saveState())