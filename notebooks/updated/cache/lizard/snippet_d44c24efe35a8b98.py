def _load_config(config_file):
    logger.debug('Config file: {}'.format(config_file))
    parser = configparser.ConfigParser()
    try:
        with config_file.open('r') as f:
            parser.read_file(f)
    except FileNotFoundError as e:
        logger.warning('Config file not found')
        parser = _use_default(config_file)
    except configparser.ParsingError as e:
        logger.warning('Error in config file: {}'.format(e))
        parser = _use_default(config_file)
    finally:
        try:
            config = _load_options(parser)
        except configparser.NoOptionError:
            parser = _use_default(config_file)
            config = _load_options(parser)
        logger.debug('Config loaded: {}'.format(config_file))
        return config