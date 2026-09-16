def import_single_vpn_path_to_all_vrfs(self, vpn_path, path_rts=None):
    LOG.debug('Importing path %s to qualifying VRFs', vpn_path)
    if not path_rts:
        LOG.info('Encountered a path with no RTs: %s', vpn_path)
        return
    interested_tables = set()
    if vpn_path.route_family == RF_IPv4_VPN:
        route_family = RF_IPv4_UC
    elif vpn_path.route_family == RF_IPv6_VPN:
        route_family = RF_IPv6_UC
    elif vpn_path.route_family == RF_L2_EVPN:
        route_family = RF_L2_EVPN
    elif vpn_path.route_family == RF_VPNv4_FLOWSPEC:
        route_family = RF_IPv4_FLOWSPEC
    elif vpn_path.route_family == RF_VPNv6_FLOWSPEC:
        route_family = RF_IPv6_FLOWSPEC
    elif vpn_path.route_family == RF_L2VPN_FLOWSPEC:
        route_family = RF_L2VPN_FLOWSPEC
    else:
        raise ValueError('Unsupported route family for VRF: %s' % vpn_path.
            route_family)
    for rt in path_rts:
        rt_rf_id = rt + ':' + str(route_family)
        vrf_rt_tables = self._tables_for_rt.get(rt_rf_id)
        if vrf_rt_tables:
            interested_tables.update(vrf_rt_tables)
    if interested_tables:
        route_dist = vpn_path.nlri.route_dist
        for vrf_table in interested_tables:
            if (vpn_path.source is not None or route_dist != vrf_table.
                vrf_conf.route_dist):
                update_vrf_dest = vrf_table.import_vpn_path(vpn_path)
                if update_vrf_dest is not None:
                    self._signal_bus.dest_changed(update_vrf_dest)
    else:
        LOG.debug('No VRF table found that imports RTs: %s', path_rts)