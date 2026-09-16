def unregister(self, plugin=None, name=None):
    if name is None:
        assert plugin is not None, 'one of name or plugin needs to be specified'
        name = self.get_name(plugin)
    if plugin is None:
        plugin = self.get_plugin(name)
    if self._name2plugin.get(name):
        del self._name2plugin[name]
    for hookcaller in self._plugin2hookcallers.pop(plugin, []):
        hookcaller._remove_plugin(plugin)
    return plugin