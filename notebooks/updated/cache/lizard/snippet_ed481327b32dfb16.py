def update_serviceprofile(self, host_id, vlan_id):
    ucsm_ip = self.get_ucsm_ip_for_host(host_id)
    if not ucsm_ip:
        LOG.info(
            'UCS Manager network driver does not have UCSM IP for Host_id %s',
            str(host_id))
        return False
    service_profile = self.ucsm_sp_dict.get((ucsm_ip, host_id))
    if service_profile:
        LOG.debug('UCS Manager network driver Service Profile : %s',
            service_profile)
    else:
        LOG.info('UCS Manager network driver does not support Host_id %s',
            host_id)
        return False
    with self.ucsm_connect_disconnect(ucsm_ip) as handle:
        if not self._create_vlanprofile(handle, vlan_id, ucsm_ip):
            LOG.error(
                'UCS Manager network driver failed to create Vlan Profile for vlan %s'
                , str(vlan_id))
            return False
        if not self._update_service_profile(handle, service_profile,
            vlan_id, ucsm_ip):
            LOG.error(
                'UCS Manager network driver failed to update Service Profile %(service_profile)s in UCSM %(ucsm_ip)s'
                , {'service_profile': service_profile, 'ucsm_ip': ucsm_ip})
            return False
    return True