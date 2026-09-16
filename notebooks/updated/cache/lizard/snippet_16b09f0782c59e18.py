def _get_host_switches(self, host_id):
    all_switches = set()
    active_switches = set()
    try:
        host_list = nxos_db.get_host_mappings(host_id)
        for mapping in host_list:
            all_switches.add(mapping.switch_ip)
            if self.is_switch_active(mapping.switch_ip):
                active_switches.add(mapping.switch_ip)
    except excep.NexusHostMappingNotFound:
        pass
    return list(all_switches), list(active_switches)