def maps_get_default_rules_output_rules_groupname(self, **kwargs):
    config = ET.Element('config')
    maps_get_default_rules = ET.Element('maps_get_default_rules')
    config = maps_get_default_rules
    output = ET.SubElement(maps_get_default_rules, 'output')
    rules = ET.SubElement(output, 'rules')
    groupname = ET.SubElement(rules, 'groupname')
    groupname.text = kwargs.pop('groupname')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)