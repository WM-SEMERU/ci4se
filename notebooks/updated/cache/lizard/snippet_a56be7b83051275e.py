def render(template, namespace, app=None):
    app = app or state.app
    return app.render(template, namespace)