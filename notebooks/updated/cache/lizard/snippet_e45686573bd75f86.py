def get_bool(self, key, default=UndefinedKey):
    bool_conversions = {None: None, 'true': True, 'yes': True, 'on': True,
        'false': False, 'no': False, 'off': False}
    string_value = self.get_string(key, default)
    if string_value is not None:
        string_value = string_value.lower()
    try:
        return bool_conversions[string_value]
    except KeyError:
        raise ConfigException('{key} does not translate to a Boolean value'
            .format(key=key))