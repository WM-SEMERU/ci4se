def load_config(configfile):
    try:
        with open(configfile, 'r') as ymlfile:
            try:
                config = yaml.load(ymlfile)
                return config
            except yaml.parser.ParserError:
                raise PyYAMLConfigError('Could not parse config file: {}'.
                    format(configfile))
    except IOError:
        raise PyYAMLConfigError('Could not open config file: {}'.format(
            configfile))