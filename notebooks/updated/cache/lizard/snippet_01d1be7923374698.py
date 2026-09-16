def snmp_server_host_source_interface_source_interface_type_loopback_loopback(
    self, **kwargs):
    config = ET.Element('config')
    snmp_server = ET.SubElement(config, 'snmp-server', xmlns=
        'urn:brocade.com:mgmt:brocade-snmp')
    host = ET.SubElement(snmp_server, 'host')
    ip_key = ET.SubElement(host, 'ip')
    ip_key.text = kwargs.pop('ip')
    community_key = ET.SubElement(host, 'community')
    community_key.text = kwargs.pop('community')
    source_interface = ET.SubElement(host, 'source-interface')
    source_interface_type = ET.SubElement(source_interface,
        'source-interface-type')
    loopback = ET.SubElement(source_interface_type, 'loopback')
    loopback = ET.SubElement(loopback, 'loopback')
    loopback.text = kwargs.pop('loopback')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)