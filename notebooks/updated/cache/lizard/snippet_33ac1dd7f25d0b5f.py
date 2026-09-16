def config_parser_to_dict(config_parser):
    response = {}
    for section in config_parser.sections():
        for option in config_parser.options(section):
            response.setdefault(section, {})[option] = config_parser.get(
                section, option)
    return response