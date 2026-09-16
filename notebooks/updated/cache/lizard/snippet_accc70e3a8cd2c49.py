def flowspec_prefix_del(self, flowspec_family, rules, route_dist=None):
    func_name = 'flowspec.del'
    kwargs = {FLOWSPEC_FAMILY: flowspec_family, FLOWSPEC_RULES: rules}
    if flowspec_family in [FLOWSPEC_FAMILY_VPNV4, FLOWSPEC_FAMILY_VPNV6,
        FLOWSPEC_FAMILY_L2VPN]:
        func_name = 'flowspec.del_local'
        kwargs.update({ROUTE_DISTINGUISHER: route_dist})
    call(func_name, **kwargs)