def use_app(backend_name=None, call_reuse=True):
    global default_app
    if default_app is not None:
        names = default_app.backend_name.lower().replace('(', ' ').strip(') ')
        names = [name for name in names.split(' ') if name]
        if backend_name and backend_name.lower() not in names:
            raise RuntimeError(
                'Can only select a backend once, already using %s.' % names)
        else:
            if call_reuse:
                default_app.reuse()
            return default_app
    default_app = Application(backend_name)
    return default_app