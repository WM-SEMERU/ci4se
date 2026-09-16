def discover():
    if CFG['plugins']['autoload']:
        experiment_plugins = CFG['plugins']['experiments'].value
        for exp_plugin in experiment_plugins:
            try:
                importlib.import_module(exp_plugin)
            except ImportError as import_error:
                LOG.error("Could not find '%s'", exp_plugin)
                LOG.error('ImportError: %s', import_error.msg)