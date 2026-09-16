def l2traceroute_input_vlan_id(self, **kwargs):
    config = ET.Element('config')
    l2traceroute = ET.Element('l2traceroute')
    config = l2traceroute
    input = ET.SubElement(l2traceroute, 'input')
    vlan_id = ET.SubElement(input, 'vlan-id')
    vlan_id.text = kwargs.pop('vlan_id')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)