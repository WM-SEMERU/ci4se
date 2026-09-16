def _update_versions():
    for pm_name in plot._plot_methods:
        pm = getattr(plot, pm_name)
        plugin = pm._plugin
        if (plugin is not None and plugin not in _versions and pm.module in
            sys.modules):
            _versions.update(get_versions(key=lambda s: s == plugin))