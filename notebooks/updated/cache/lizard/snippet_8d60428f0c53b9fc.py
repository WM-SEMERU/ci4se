def get_lldp_neighbor_detail_output_has_more(self, **kwargs):
    config = ET.Element('config')
    get_lldp_neighbor_detail = ET.Element('get_lldp_neighbor_detail')
    config = get_lldp_neighbor_detail
    output = ET.SubElement(get_lldp_neighbor_detail, 'output')
    has_more = ET.SubElement(output, 'has-more')
    has_more.text = kwargs.pop('has_more')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)