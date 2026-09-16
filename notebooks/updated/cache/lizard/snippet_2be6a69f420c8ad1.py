def get(property_name):
    config = _read_config(_USER_CONFIG_FILE)
    section = _MAIN_SECTION_NAME
    try:
        property_value = config.get(section, property_name)
    except (NoOptionError, NoSectionError) as error:
        try:
            config = _read_config(_SYSTEM_CONFIG_FILE)
            property_value = config.get(section, property_name)
        except (NoOptionError, NoSectionError) as error:
            raise NoConfigOptionError(error)
    return property_value