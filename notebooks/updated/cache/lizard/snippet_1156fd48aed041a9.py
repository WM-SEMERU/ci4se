def get_config_value(config_file, section, variable):
    try:
        parser = ConfigParser.SafeConfigParser()
        parser.read(config_file)
        return parser.get(section, variable)
    except:
        return None