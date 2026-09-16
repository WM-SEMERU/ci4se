def get_plugin(self, method):
    all_plugins = []
    for entry_point in pkg_resources.iter_entry_points('yolk.plugins'):
        plugin_obj = entry_point.load()
        plugin = plugin_obj()
        plugin.configure(self.options, None)
        if plugin.enabled:
            if not hasattr(plugin, method):
                self.logger.warn('Error: plugin has no method: %s' % method)
                plugin = None
            else:
                all_plugins.append(plugin)
    return all_plugins