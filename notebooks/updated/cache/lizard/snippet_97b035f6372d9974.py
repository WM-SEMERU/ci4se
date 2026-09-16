def load(klass):
    config = klass()
    for path in klass.CONF_PATHS:
        if os.path.exists(path):
            with open(path, 'r') as conf:
                config.configure(yaml.safe_load(conf))
    return config