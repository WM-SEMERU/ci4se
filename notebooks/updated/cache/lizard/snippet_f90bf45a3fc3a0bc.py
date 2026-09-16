def system_switch_attributes_rbridge_id_rbridge_id(self, **kwargs):
    config = ET.Element('config')
    system = ET.SubElement(config, 'system', xmlns=
        'urn:brocade.com:mgmt:brocade-ras')
    switch_attributes = ET.SubElement(system, 'switch-attributes')
    rbridge_id = ET.SubElement(switch_attributes, 'rbridge-id')
    rbridge_id = ET.SubElement(rbridge_id, 'rbridge-id')
    rbridge_id.text = kwargs.pop('rbridge_id')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)