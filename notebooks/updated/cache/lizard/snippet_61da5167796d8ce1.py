def configure_api(app, manager):
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    app.extensions['babbage'] = manager
    return blueprint