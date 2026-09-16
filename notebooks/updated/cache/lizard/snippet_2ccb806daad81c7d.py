def restoreSettings(self, settings):
    value = unwrapVariant(settings.value('recent_files'))
    if value:
        self.setFilenames(value.split(os.path.pathsep))