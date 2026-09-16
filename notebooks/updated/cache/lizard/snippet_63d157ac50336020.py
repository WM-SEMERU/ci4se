def create_network(self, name, admin_state_up=True, router_ext=None,
    network_type=None, physical_network=None, segmentation_id=None, shared=
    None, vlan_transparent=None):
    body = {'name': name, 'admin_state_up': admin_state_up}
    if router_ext:
        body['router:external'] = router_ext
    if network_type:
        body['provider:network_type'] = network_type
    if physical_network:
        body['provider:physical_network'] = physical_network
    if segmentation_id:
        body['provider:segmentation_id'] = segmentation_id
    if shared:
        body['shared'] = shared
    if vlan_transparent:
        body['vlan_transparent'] = vlan_transparent
    return self.network_conn.create_network(body={'network': body})