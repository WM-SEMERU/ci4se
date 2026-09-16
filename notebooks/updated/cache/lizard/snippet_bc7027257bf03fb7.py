def converter_loader(app, entry_points=None, modules=None):
    if entry_points:
        for entry_point in entry_points:
            for ep in pkg_resources.iter_entry_points(entry_point):
                try:
                    app.url_map.converters[ep.name] = ep.load()
                except Exception:
                    app.logger.error('Failed to initialize entry point: {0}'
                        .format(ep))
                    raise
    if modules:
        app.url_map.converters.update(**modules)