def get_network_stats(self, tags):
    if is_affirmative(self.init_config.get('check_all_networks', True)):
        all_network_ids = set(self.get_all_network_ids())
        network_ids = [network_id for network_id in all_network_ids if not
            any([re.match(exclude_id, network_id) for exclude_id in self.
            exclude_network_id_rules])]
    else:
        network_ids = self.init_config.get('network_ids', [])
    if not network_ids:
        self.warning(
            'Your check is not configured to monitor any networks.\n' +
            'Please list `network_ids` under your init_config')
    for nid in network_ids:
        self.get_stats_for_single_network(nid, tags)