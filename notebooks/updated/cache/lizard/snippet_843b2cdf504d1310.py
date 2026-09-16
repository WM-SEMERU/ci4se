def l2traceroute_input_dest_mac(self, **kwargs):
    config = ET.Element('config')
    l2traceroute = ET.Element('l2traceroute')
    config = l2traceroute
    input = ET.SubElement(l2traceroute, 'input')
    dest_mac = ET.SubElement(input, 'dest-mac')
    dest_mac.text = kwargs.pop('dest_mac')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)