def check_for_missing_options(config):
    for section_name, section in config:
        for option_name, option in section:
            if option.required and option.value is None:
                raise exc.MissingRequiredOption(
                    'Option {0} in namespace {1} is required.'.format(
                    option_name, section_name))
    return config