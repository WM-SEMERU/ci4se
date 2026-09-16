def get_scenario_host_ip_on_network(self, scenario_role_name, network_name):
    log = logging.getLogger(self.cls_logger +
        '.get_scenario_host_ip_on_network')
    cons3rt_network_info = None
    for scenario_host in self.scenario_network_info:
        if scenario_host['scenario_role_name'] == scenario_role_name:
            cons3rt_network_info = scenario_host['network_info']
    if not cons3rt_network_info:
        log.warn('Unable to find network info for this host')
        return
    internal_ip = None
    for cons3rt_network in cons3rt_network_info:
        if cons3rt_network['network_name'] == network_name:
            internal_ip = cons3rt_network['internal_ip']
    if not internal_ip:
        log.warn('Unable to find an internal IP for network: {n}'.format(n=
            network_name))
        return
    log.debug('Found IP address [{i}] for network name: {n}'.format(i=
        internal_ip, n=network_name))
    return internal_ip