def initialise_by_names(self, plugins=None):
    if plugins is None:
        plugins = []
    self._log.debug('Plugins Initialisation started')
    if not isinstance(plugins, list):
        raise AttributeError('plugins must be a list, not %s' % type(plugins))
    self._log.debug('Plugins to initialise: %s' % ', '.join(plugins))
    plugin_initialised = []
    for plugin_name in plugins:
        if not isinstance(plugin_name, str):
            raise AttributeError('plugin name must be a str, not %s' % type
                (plugin_name))
        plugin_class = self.classes.get(plugin_name)
        self.initialise(plugin_class.clazz, plugin_name)
        plugin_initialised.append(plugin_name)
    self._log.info('Plugins initialised: %s' % ', '.join(plugin_initialised))