def create_and_link_vrf_table(self, vrf_conf):
    route_family = vrf_conf.route_family
    if route_family == VRF_RF_IPV4:
        vrf_table = Vrf4Table
    elif route_family == VRF_RF_IPV6:
        vrf_table = Vrf6Table
    elif route_family == VRF_RF_L2_EVPN:
        vrf_table = VrfEvpnTable
    elif route_family == VRF_RF_IPV4_FLOWSPEC:
        vrf_table = Vrf4FlowSpecTable
    elif route_family == VRF_RF_IPV6_FLOWSPEC:
        vrf_table = Vrf6FlowSpecTable
    elif route_family == VRF_RF_L2VPN_FLOWSPEC:
        vrf_table = L2vpnFlowSpecTable
    else:
        raise ValueError('Unsupported route family for VRF: %s' % route_family)
    vrf_table = vrf_table(vrf_conf, self._core_service, self._signal_bus)
    table_id = vrf_conf.route_dist, route_family
    self._tables[table_id] = vrf_table
    assert vrf_table is not None
    LOG.debug('Added new VrfTable with route_dist:%s and route_family:%s',
        vrf_conf.route_dist, route_family)
    import_rts = vrf_conf.import_rts
    if import_rts:
        self._link_vrf_table(vrf_table, import_rts)
    return vrf_table