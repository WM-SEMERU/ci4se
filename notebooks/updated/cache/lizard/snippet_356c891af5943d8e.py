def get_registered_instances(self, include_removed=False):
    rval = []
    configs = self.state.get('config_files', {}).values()
    if include_removed:
        configs.extend(self.state.get('remove_configs', {}).values())
    for config in configs:
        if config['instance_name'] not in rval:
            rval.append(config['instance_name'])
    return rval