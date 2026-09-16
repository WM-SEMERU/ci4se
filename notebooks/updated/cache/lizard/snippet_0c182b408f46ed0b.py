def get_roots(app=None):
    roots = set()
    plugins = app.config['PLUGINS'] if app else None
    for name in ENTRYPOINTS.keys():
        for ep in iter_all(name):
            if plugins is None or ep.name in plugins:
                roots.add(ep.module_name.split('.', 1)[0])
    return list(roots)