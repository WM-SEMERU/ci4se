def set_analysis_config(self, group_name, config):
    self.assert_writeable()
    if 'Analyses/{}'.format(group_name) not in self.handle:
        msg = (
            'Dataset cannot be added to non-existent group: Analyses/{} in {}')
        raise KeyError(msg.format(group_name, self.filename))
    if isinstance(config, ConfigParser):
        config_dict = {}
        for section in config.sections():
            config_dict[section] = {k: v for k, v in config.items(section)}
    elif isinstance(config, dict):
        config_dict = config
    else:
        raise TypeError('config must be a ConfigParser or dict not {}'.
            format(type(config)))
    config_path = 'Analyses/{}/Configuration'.format(group_name)
    self._add_attribute_tree(config_path, config_dict)