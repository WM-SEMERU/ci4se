def load_plugin_by_name(name):
    plugins = load(PLUGIN_NAMESPACE)
    full_name = '%s.%s' % (PLUGIN_NAMESPACE, name)
    try:
        plugins = (plugin for plugin in plugins if plugin.__name__ == full_name
            )
        plugin = next(plugins)
        return plugin
    except StopIteration:
        raise UnknownPlugin([plugin.__name__.split('.').pop() for plugin in
            plugins])