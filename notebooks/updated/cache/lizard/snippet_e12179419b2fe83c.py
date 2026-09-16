def autodiscover(path=None, plugin_prefix='intake_'):
    plugins = {}
    for importer, name, ispkg in pkgutil.iter_modules(path=path):
        if name.startswith(plugin_prefix):
            t = time.time()
            new_plugins = load_plugins_from_module(name)
            for plugin_name, plugin in new_plugins.items():
                if plugin_name in plugins:
                    orig_path = inspect.getfile(plugins[plugin_name])
                    new_path = inspect.getfile(plugin)
                    warnings.warn(
                        """Plugin name collision for "%s" from
    %s
and
    %s
Keeping plugin from first location."""
                         % (plugin_name, orig_path, new_path))
                else:
                    plugins[plugin_name] = plugin
            logger.debug('Import %s took: %7.2f s' % (name, time.time() - t))
    return plugins