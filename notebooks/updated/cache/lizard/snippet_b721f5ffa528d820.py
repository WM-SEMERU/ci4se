def update(self, settings):
    self.settings.cache_clear()
    self._settings = settings
    log.info('Updated settings to %s', self._settings)
    self._update_disabled_plugins()