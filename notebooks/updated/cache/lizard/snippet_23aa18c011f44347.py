def _create_vlanprofile(self, handle, vlan_id, ucsm_ip):
    vlan_name = self.make_vlan_name(vlan_id)
    vlan_profile_dest = (const.VLAN_PATH + const.VLAN_PROFILE_PATH_PREFIX +
        vlan_name)
    try:
        vp1 = handle.query_dn(const.VLAN_PATH)
        if not vp1:
            LOG.warning(
                'UCS Manager network driver Vlan Profile path at %s missing',
                const.VLAN_PATH)
            return False
        vp2 = self.ucsmsdk.fabricVlan(parent_mo_or_dn=vp1, name=vlan_name,
            compression_type=const.VLAN_COMPRESSION_TYPE, sharing=const.
            NONE, pub_nw_name='', id=str(vlan_id), mcast_policy_name='',
            default_net='no')
        handle.add_mo(vp2)
        handle.commit()
        if vp2:
            LOG.debug(
                'UCS Manager network driver Created Vlan Profile %s at %s',
                vlan_name, vlan_profile_dest)
            return True
    except Exception as e:
        return self._handle_ucsm_exception(e, 'Vlan Profile', vlan_name,
            ucsm_ip)