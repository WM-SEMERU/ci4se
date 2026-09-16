def ip_rtm_config_route_static_route_oif_vrf_static_route_oif_name(self, **
    kwargs):
    config = ET.Element('config')
    ip = ET.SubElement(config, 'ip', xmlns=
        'urn:brocade.com:mgmt:brocade-common-def')
    rtm_config = ET.SubElement(ip, 'rtm-config', xmlns=
        'urn:brocade.com:mgmt:brocade-rtm')
    route = ET.SubElement(rtm_config, 'route')
    static_route_oif_vrf = ET.SubElement(route, 'static-route-oif-vrf')
    static_route_next_vrf_dest_key = ET.SubElement(static_route_oif_vrf,
        'static-route-next-vrf-dest')
    static_route_next_vrf_dest_key.text = kwargs.pop(
        'static_route_next_vrf_dest')
    next_hop_vrf_key = ET.SubElement(static_route_oif_vrf, 'next-hop-vrf')
    next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
    static_route_oif_type_key = ET.SubElement(static_route_oif_vrf,
        'static-route-oif-type')
    static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
    static_route_oif_name = ET.SubElement(static_route_oif_vrf,
        'static-route-oif-name')
    static_route_oif_name.text = kwargs.pop('static_route_oif_name')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)