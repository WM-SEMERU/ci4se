def get_lldp_neighbor_detail_input_request_type_get_rbridge_specific_rbridge_id(
    self, **kwargs):
    config = ET.Element('config')
    get_lldp_neighbor_detail = ET.Element('get_lldp_neighbor_detail')
    config = get_lldp_neighbor_detail
    input = ET.SubElement(get_lldp_neighbor_detail, 'input')
    request_type = ET.SubElement(input, 'request-type')
    get_rbridge_specific = ET.SubElement(request_type, 'get-rbridge-specific')
    rbridge_id = ET.SubElement(get_rbridge_specific, 'rbridge-id')
    rbridge_id.text = kwargs.pop('rbridge_id')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)