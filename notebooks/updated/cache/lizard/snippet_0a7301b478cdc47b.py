def unprovision_vdp_overlay_networks(self, net_uuid, lvid, vdp_vlan, oui):
    if not ovs_lib.is_valid_vlan_tag(vdp_vlan):
        LOG.error(
            'Cannot unprovision VDP Overlay network for net-id=%(net_uuid)s - Invalid '
            , {'net_uuid': net_uuid})
        return
    LOG.info(
        'unprovision_vdp_overlay_networks: add_flow for Local Vlan %(local_vlan)s VDP VLAN %(vdp_vlan)s'
        , {'local_vlan': lvid, 'vdp_vlan': vdp_vlan})
    self.program_vm_ovs_flows(lvid, vdp_vlan, 0)