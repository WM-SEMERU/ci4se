def get_paths(cls, packages):
    allowable_packages = dict((app_config.name, app_config) for app_config in
        apps.get_app_configs())
    app_configs = [allowable_packages[p] for p in packages if p in
        allowable_packages]
    return [os.path.join(app.path, 'locale') for app in app_configs]