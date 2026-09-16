def disable_plugin(plugin_name):
    if isinstance(plugin_name, types.StringTypes):
        plugin_name = [plugin_name]
    enabled_path = MICRODROP_CONDA_PLUGINS.joinpath('enabled')
    for name_i in plugin_name:
        plugin_path_i = enabled_path.joinpath(name_i)
        if not _islinklike(plugin_path_i) and not plugin_path_i.isdir():
            raise IOError('Plugin `{}` not found in `{}`'.format(name_i,
                enabled_path))
    for name_i in plugin_name:
        plugin_link_path_i = enabled_path.joinpath(name_i)
        plugin_link_path_i.unlink()
        logger.debug('Disabled plugin `%s` (i.e., removed `%s`)',
            plugin_path_i, plugin_link_path_i)