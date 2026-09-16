def cee_map_remap_lossless_priority_lossless_remapped_priority(self, **kwargs):
    config = ET.Element('config')
    cee_map = ET.SubElement(config, 'cee-map', xmlns=
        'urn:brocade.com:mgmt:brocade-cee-map')
    name_key = ET.SubElement(cee_map, 'name')
    name_key.text = kwargs.pop('name')
    remap = ET.SubElement(cee_map, 'remap')
    lossless_priority = ET.SubElement(remap, 'lossless-priority')
    lossless_remapped_priority = ET.SubElement(lossless_priority,
        'lossless-remapped-priority')
    lossless_remapped_priority.text = kwargs.pop('lossless_remapped_priority')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)