def get_config_value(self, overrides, skip_environment=False):
    label, override, key = self._search_overrides(overrides, skip_environment)
    if override is None and self.default is None and self.required:
        raise YapconfItemNotFound('Could not find config value for {0}'.
            format(self.fq_name), self)
    if override is None:
        self.logger.debug(
            'Config value not found for {0}, falling back to default.'.
            format(self.name))
        value = self.default
    else:
        value = override[key]
    if value is None:
        return value
    converted_value = self.convert_config_value(value, label)
    self._validate_value(converted_value)
    return converted_value