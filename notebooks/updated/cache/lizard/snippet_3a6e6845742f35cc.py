def set_json(self, config_json):
    if self.configuration_dict is not None:
        raise RuntimeError('Can only set configuration once', self.
            configuration_dict)
    schema = fetch_config('ConfigurationSchema.json')
    validictory.validate(config_json, schema)
    config_json['name'] = self.name
    config_json['run_number'] = self.run
    config_json['src_dir'] = get_source_dir()
    config_json['data_dir'] = get_data_dir()
    config_json['log_dir'] = get_log_dir()
    self.configuration_dict = config_json