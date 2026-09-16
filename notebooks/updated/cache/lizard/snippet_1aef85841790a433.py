def init_config(app):
    for k in dir(config):
        if k.startswith('CLASSIFIER_'):
            app.config.setdefault(k, getattr(config, k))