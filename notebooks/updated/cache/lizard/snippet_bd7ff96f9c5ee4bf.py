def get_configparser(filename=''):
    filename = filename or os.environ.get('SHELTER_CONFIG_FILENAME', '')
    if not filename:
        raise ImproperlyConfiguredError(_(
            "Configuration file is not defined. You must either set 'SHELTER_CONFIG_FILENAME' environment variable or '-f/--config-file' command line argument."
            ))
    parser = six.moves.configparser.RawConfigParser()
    for conf_file in get_conf_files(filename):
        logger.info("Found config '%s'", conf_file)
        if not parser.read(conf_file):
            logger.warning("Error while parsing config '%s'", conf_file)
    return parser