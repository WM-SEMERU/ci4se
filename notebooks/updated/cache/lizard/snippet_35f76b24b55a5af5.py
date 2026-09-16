def _default_plugins(self):
    plugins = {}
    try:
        with open('entry_points.json') as f:
            entry_points = json.load(f)
        for ep, obj in entry_points.items():
            plugins[ep] = []
            for name, src in obj.items():
                plugins[ep].append(Plugin(name=name, source=src))
    except Exception as e:
        print('Failed to load entry points {}'.format(e))
    return plugins