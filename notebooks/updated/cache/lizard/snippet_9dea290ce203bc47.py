def create_basic_app(cls, bundles=None, _config_overrides=None):
    bundles = bundles or []
    name = bundles[-1].module_name if bundles else 'basic_app'
    app = FlaskUnchained(name, template_folder=os.path.join(os.path.dirname
        (__file__), 'templates'))
    for bundle in bundles:
        bundle.before_init_app(app)
    unchained.init_app(app, DEV, bundles, _config_overrides=_config_overrides)
    for bundle in bundles:
        bundle.after_init_app(app)
    return app