def create(cls, config_file=None):
    if cls.instance is None:
        cls.instance = cls(config_file)
        cls.instance.load_ini()
    if config_file and config_file != cls.instance.config_file:
        raise RuntimeError(
            'Configuration initialized a second time with a different file!')
    return cls.instance