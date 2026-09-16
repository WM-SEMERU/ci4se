def make_app(global_conf, full_stack=True, **app_conf):
    load_environment(global_conf, app_conf)
    app = PylonsApp()
    app = AuthMiddleware(app)
    app = RoutesMiddleware(app, config['routes.map'])
    app = SessionMiddleware(app, config)
    app = CacheMiddleware(app, config)
    if asbool(full_stack):
        app = ErrorHandler(app, global_conf, **config['pylons.errorware'])
        if asbool(config['debug']):
            app = StatusCodeRedirect(app)
        else:
            app = StatusCodeRedirect(app, [400, 401, 403, 404, 500])
    app = RegistryManager(app)
    static_app = StaticURLParser(config['pylons.paths']['static_files'])
    app = Cascade([static_app, app])
    return app