def configure_filters(app):
    for name, filter in _filters.iteritems():
        app.jinja_env.filters[name] = filter