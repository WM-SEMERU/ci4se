def _convert_topo_obj_dict(self, topology_objs):
    topo_lst = []
    for topo_obj in topology_objs:
        topo_dct = {'host': topo_obj.host, 'protocol_interface': topo_obj.
            protocol_interface, 'phy_interface': topo_obj.phy_interface,
            'created': topo_obj.created, 'heartbeat': topo_obj.heartbeat,
            'remote_mgmt_addr': topo_obj.remote_mgmt_addr,
            'remote_system_name': topo_obj.remote_system_name,
            'remote_system_desc': topo_obj.remote_system_desc,
            'remote_port_id_mac': topo_obj.remote_port_id_mac,
            'remote_chassis_id_mac': topo_obj.remote_chassis_id_mac,
            'remote_port': topo_obj.remote_port, 'remote_evb_cfgd':
            topo_obj.remote_evb_cfgd, 'remote_evb_mode': topo_obj.
            remote_evb_mode, 'configurations': topo_obj.configurations}
        topo_lst.append(topo_dct)
    return topo_lst