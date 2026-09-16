def add_router_interface(self, context, router_id, interface_info):
    new_router = super(AristaL3ServicePlugin, self).add_router_interface(
        context, router_id, interface_info)
    core = directory.get_plugin()
    add_by_port, add_by_sub = self._validate_interface_info(interface_info)
    if add_by_sub:
        subnet = core.get_subnet(context, interface_info['subnet_id'])
    elif add_by_port:
        port = core.get_port(context, interface_info['port_id'])
        subnet_id = port['fixed_ips'][0]['subnet_id']
        subnet = core.get_subnet(context, subnet_id)
    network_id = subnet['network_id']
    ml2_db = NetworkContext(self, context, {'id': network_id})
    seg_id = ml2_db.network_segments[0]['segmentation_id']
    router = self.get_router(context, router_id)
    router_info = copy.deepcopy(new_router)
    router_info['seg_id'] = seg_id
    router_info['name'] = router['name']
    router_info['cidr'] = subnet['cidr']
    router_info['gip'] = subnet['gateway_ip']
    router_info['ip_version'] = subnet['ip_version']
    try:
        self.driver.add_router_interface(context, router_info)
        return new_router
    except Exception:
        with excutils.save_and_reraise_exception():
            LOG.error(_LE(
                'Error Adding subnet %(subnet)s to router %(router_id)s on Arista HW'
                ), {'subnet': subnet, 'router_id': router_id})
            super(AristaL3ServicePlugin, self).remove_router_interface(context,
                router_id, interface_info)