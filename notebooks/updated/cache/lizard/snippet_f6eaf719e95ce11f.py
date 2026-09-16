def handle_get_vts_command(self, vt_et):
    vt_id = vt_et.attrib.get('vt_id')
    vt_filter = vt_et.attrib.get('filter')
    if vt_id and vt_id not in self.vts:
        text = "Failed to find vulnerability test '{0}'".format(vt_id)
        return simple_response_str('get_vts', 404, text)
    filtered_vts = None
    if vt_filter:
        filtered_vts = self.vts_filter.get_filtered_vts_list(self.vts,
            vt_filter)
    responses = []
    vts_xml = self.get_vts_xml(vt_id, filtered_vts)
    responses.append(vts_xml)
    return simple_response_str('get_vts', 200, 'OK', responses)