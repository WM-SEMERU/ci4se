def ip_rtm_config_route_static_route_oif_static_route_dest(self, **kwargs):
    config = ET.Element('config')
    ip = ET.SubElement(config, 'ip', xmlns=
        'urn:brocade.com:mgmt:brocade-common-def')
    rtm_config = ET.SubElement(ip, 'rtm-config', xmlns=
        'urn:brocade.com:mgmt:brocade-rtm')
    route = ET.SubElement(rtm_config, 'route')
    static_route_oif = ET.SubElement(route, 'static-route-oif')
    static_route_oif_type_key = ET.SubElement(static_route_oif,
        'static-route-oif-type')
    static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
    static_route_oif_name_key = ET.SubElement(static_route_oif,
        'static-route-oif-name')
    static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
    static_route_dest = ET.SubElement(static_route_oif, 'static-route-dest')
    static_route_dest.text = kwargs.pop('static_route_dest')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)