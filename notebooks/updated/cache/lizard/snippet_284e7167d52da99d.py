def update_flowspec_vrf_table(self, flowspec_family, route_dist, rules,
    actions=None, is_withdraw=False):
    from ryu.services.protocols.bgp.core import BgpCoreError
    from ryu.services.protocols.bgp.api.prefix import FLOWSPEC_FAMILY_VPNV4, FLOWSPEC_FAMILY_VPNV6, FLOWSPEC_FAMILY_L2VPN
    if flowspec_family == FLOWSPEC_FAMILY_VPNV4:
        vrf_table = self._tables.get((route_dist, VRF_RF_IPV4_FLOWSPEC))
        prefix = FlowSpecIPv4NLRI.from_user(**rules)
        try:
            communities = create_v4flowspec_actions(actions)
        except ValueError as e:
            raise BgpCoreError(desc=str(e))
    elif flowspec_family == FLOWSPEC_FAMILY_VPNV6:
        vrf_table = self._tables.get((route_dist, VRF_RF_IPV6_FLOWSPEC))
        prefix = FlowSpecIPv6NLRI.from_user(**rules)
        try:
            communities = create_v6flowspec_actions(actions)
        except ValueError as e:
            raise BgpCoreError(desc=str(e))
    elif flowspec_family == FLOWSPEC_FAMILY_L2VPN:
        vrf_table = self._tables.get((route_dist, VRF_RF_L2VPN_FLOWSPEC))
        prefix = FlowSpecL2VPNNLRI.from_user(route_dist, **rules)
        try:
            communities = create_l2vpnflowspec_actions(actions)
        except ValueError as e:
            raise BgpCoreError(desc=str(e))
    else:
        raise BgpCoreError(desc='Unsupported flowspec_family %s' %
            flowspec_family)
    if vrf_table is None:
        raise BgpCoreError(desc=
            'VRF table does not exist: route_dist=%s, flowspec_family=%s' %
            (route_dist, flowspec_family))
    vrf_table.insert_vrffs_path(nlri=prefix, communities=communities,
        is_withdraw=is_withdraw)