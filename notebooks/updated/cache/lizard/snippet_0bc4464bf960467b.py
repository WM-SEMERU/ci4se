def create_portprofile(self, profile_name, vlan_id, vnic_type, host_id,
    trunk_vlans):
    ucsm_ip = self.get_ucsm_ip_for_host(host_id)
    if not ucsm_ip:
        LOG.info(
            'UCS Manager network driver does not have UCSM IP for Host_id %s',
            str(host_id))
        return False
    with self.ucsm_connect_disconnect(ucsm_ip) as handle:
        if not self._create_vlanprofile(handle, vlan_id, ucsm_ip):
            LOG.error(
                'UCS Manager network driver failed to create Vlan Profile for vlan %s'
                , str(vlan_id))
            return False
        if trunk_vlans:
            for vlan in trunk_vlans:
                if not self._create_vlanprofile(handle, vlan, ucsm_ip):
                    LOG.error(
                        'UCS Manager network driver failed to create Vlan Profile for vlan %s'
                        , vlan)
                    return False
        qos_policy = CONF.ml2_cisco_ucsm.ucsms[ucsm_ip].sriov_qos_policy
        if qos_policy:
            LOG.debug(
                'UCS Manager Network driver applying QoS Policy %(qos)s to Port Profile %(port_profile)s'
                , {'qos': qos_policy, 'port_profile': profile_name})
        if not self._create_port_profile(handle, profile_name, vlan_id,
            vnic_type, ucsm_ip, trunk_vlans, qos_policy):
            LOG.error(
                'UCS Manager network driver failed to create Port Profile %s',
                profile_name)
            return False
    return True