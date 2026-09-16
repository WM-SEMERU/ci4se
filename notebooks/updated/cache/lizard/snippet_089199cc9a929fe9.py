def check_config_options(_class, required_options, optional_options, options):
    for opt in required_options:
        if opt not in options:
            msg = 'Required option missing: {0}'
            raise ConfigurationError(msg.format(opt))
    for opt in options:
        if opt not in required_options + optional_options:
            msg = 'Unknown config option to `{0}`: {1}'
            _logger.warn(msg.format(_class, opt))