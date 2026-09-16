def _prepare_uimodules(self):
    for key, value in self._config.get(config.UI_MODULES, {}).iteritems():
        self._config[config.UI_MODULES][key] = self._import_class(value)
    self._config[config.UI_MODULES] = dict(self._config[config.UI_MODULES] or
        {})