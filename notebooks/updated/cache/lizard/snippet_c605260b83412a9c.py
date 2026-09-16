def read_config(config_filepath, logger=logging.getLogger('ProsperCommon')):
    config_parser = configparser.ConfigParser(interpolation=
        ExtendedInterpolation(), allow_no_value=True, delimiters='=',
        inline_comment_prefixes='#')
    logger.debug('config_filepath=%s', config_filepath)
    with open(config_filepath, 'r') as filehandle:
        config_parser.read_file(filehandle)
    return config_parser