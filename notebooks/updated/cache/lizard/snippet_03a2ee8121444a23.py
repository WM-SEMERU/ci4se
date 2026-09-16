def describe_config_variable(self, config_id):
    config = self._config_variables.get(config_id)
    if config is None:
        return [Error.INVALID_ARRAY_KEY, 0, 0, 0, 0]
    packed_size = config.total_size
    packed_size |= int(config.variable) << 15
    return [0, 0, 0, config_id, packed_size]