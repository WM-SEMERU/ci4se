def set_neighbor_out_filter(neigh_ip_address, filters):
    core = CORE_MANAGER.get_core_service()
    peer = core.peer_manager.get_by_addr(neigh_ip_address)
    peer.out_filters = filters
    return True