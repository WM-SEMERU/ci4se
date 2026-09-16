def _configure_port_binding(self, is_provider_vlan, duplicate_type,
    is_native, switch_ip, vlan_id, intf_type, nexus_port, vni):
    if duplicate_type == const.DUPLICATE_PORT:
        return
    auto_create, auto_trunk = self._gather_config_parms(is_provider_vlan,
        vlan_id)
    if duplicate_type == const.DUPLICATE_VLAN:
        auto_create = False
    if auto_create and auto_trunk:
        LOG.debug('Nexus: create vlan %s and add to interface', vlan_id)
        self.driver.create_and_trunk_vlan(switch_ip, vlan_id, intf_type,
            nexus_port, vni, is_native)
    elif auto_create:
        LOG.debug('Nexus: create vlan %s', vlan_id)
        self.driver.create_vlan(switch_ip, vlan_id, vni)
    elif auto_trunk:
        LOG.debug('Nexus: trunk vlan %s', vlan_id)
        self.driver.send_enable_vlan_on_trunk_int(switch_ip, vlan_id,
            intf_type, nexus_port, is_native)