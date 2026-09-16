def qos_map_cos_traffic_class_cos4(self, **kwargs):
    config = ET.Element('config')
    qos = ET.SubElement(config, 'qos', xmlns='urn:brocade.com:mgmt:brocade-qos'
        )
    map = ET.SubElement(qos, 'map')
    cos_traffic_class = ET.SubElement(map, 'cos-traffic-class')
    name_key = ET.SubElement(cos_traffic_class, 'name')
    name_key.text = kwargs.pop('name')
    cos4 = ET.SubElement(cos_traffic_class, 'cos4')
    cos4.text = kwargs.pop('cos4')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)