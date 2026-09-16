def get_versions(requirements=True, key=None):
    from pkg_resources import iter_entry_points
    ret = {'psyplot': _get_versions(requirements)}
    for ep in iter_entry_points(group='psyplot', name='plugin'):
        if str(ep) in rcParams._plugins:
            logger.debug('Loading entrypoint %s', ep)
            if key is not None and not key(ep.module_name):
                continue
            mod = ep.load()
            try:
                ret[str(ep.module_name)] = mod.get_versions(requirements)
            except AttributeError:
                ret[str(ep.module_name)] = {'version': getattr(mod,
                    'plugin_version', getattr(mod, '__version__', ''))}
    if key is None:
        try:
            import psyplot_gui
        except ImportError:
            pass
        else:
            ret['psyplot_gui'] = psyplot_gui.get_versions(requirements)
    return ret