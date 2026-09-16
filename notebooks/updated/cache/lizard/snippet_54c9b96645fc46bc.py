def set_neighbor_attribute_map(neigh_ip_address, at_maps, route_dist=None,
    route_family=VRF_RF_IPV4):
    core = CORE_MANAGER.get_core_service()
    peer = core.peer_manager.get_by_addr(neigh_ip_address)
    at_maps_key = const.ATTR_MAPS_LABEL_DEFAULT
    at_maps_dict = {}
    if route_dist is not None:
        vrf_conf = CORE_MANAGER.vrfs_conf.get_vrf_conf(route_dist, route_family
            )
        if vrf_conf:
            at_maps_key = ':'.join([route_dist, route_family])
        else:
            raise RuntimeConfigError(desc='No VrfConf with rd %s' % route_dist)
    at_maps_dict[const.ATTR_MAPS_LABEL_KEY] = at_maps_key
    at_maps_dict[const.ATTR_MAPS_VALUE] = at_maps
    peer.attribute_maps = at_maps_dict
    return True