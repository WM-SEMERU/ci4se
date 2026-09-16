def inspect(self):
    if not self.client_config.features['networks']:
        raise ValueError('Client does not support network configuration.',
            self.client_name)
    config_id = self.config_id
    network_name = self.network_name = self.policy.nname(config_id.map_name,
        config_id.config_name)
    if network_name in self.policy.network_names[self.client_name]:
        self.detail = self.client.inspect_network(network_name)
    else:
        self.detail = NOT_FOUND