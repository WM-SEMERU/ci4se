def release_plugin(self, name):
    plugin = self._active_plugins[name]
    if id(plugin) in self._provided_by_preset:
        self._provided_by_preset.remove(id(plugin))
    del self._active_plugins[name]
    delattr(self, name)