def _update_redundancy_router_interfaces(self, context, router, port,
    modified_port_data, redundancy_router_ids=None, ha_settings_db=None):
    router_id = router['id']
    if ha_settings_db is None:
        ha_settings_db = self._get_ha_settings_by_router_id(context, router_id)
    if ha_settings_db is None:
        return
    e_context = context.elevated()
    rr_ids = self._get_redundancy_router_ids(e_context, router_id)
    port_info_list = self._core_plugin.get_ports(e_context, filters={
        'device_id': rr_ids, 'network_id': [port['network_id']]}, fields=[
        'device_id', 'id'])
    for port_info in port_info_list:
        self._core_plugin.update_port(e_context, port_info['id'],
            modified_port_data)
    self._update_hidden_port(e_context, port['id'], modified_port_data)