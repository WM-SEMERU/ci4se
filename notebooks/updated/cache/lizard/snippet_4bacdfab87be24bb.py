def hide_routemap_holder_route_map_content_set_ipv6_interface_ipv6_null0(self,
    **kwargs):
    config = ET.Element('config')
    hide_routemap_holder = ET.SubElement(config, 'hide-routemap-holder',
        xmlns='urn:brocade.com:mgmt:brocade-ip-policy')
    route_map = ET.SubElement(hide_routemap_holder, 'route-map')
    name_key = ET.SubElement(route_map, 'name')
    name_key.text = kwargs.pop('name')
    action_rm_key = ET.SubElement(route_map, 'action-rm')
    action_rm_key.text = kwargs.pop('action_rm')
    instance_key = ET.SubElement(route_map, 'instance')
    instance_key.text = kwargs.pop('instance')
    content = ET.SubElement(route_map, 'content')
    set = ET.SubElement(content, 'set')
    ipv6 = ET.SubElement(set, 'ipv6')
    interface = ET.SubElement(ipv6, 'interface')
    ipv6_null0 = ET.SubElement(interface, 'ipv6-null0')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)