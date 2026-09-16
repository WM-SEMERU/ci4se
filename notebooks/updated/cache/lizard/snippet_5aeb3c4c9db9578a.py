def remove_page(self, process_id, wit_ref_name, page_id):
    route_values = {}
    if process_id is not None:
        route_values['processId'] = self._serialize.url('process_id',
            process_id, 'str')
    if wit_ref_name is not None:
        route_values['witRefName'] = self._serialize.url('wit_ref_name',
            wit_ref_name, 'str')
    if page_id is not None:
        route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
    self._send(http_method='DELETE', location_id=
        '1cc7b29f-6697-4d9d-b0a1-2650d3e1d584', version='5.0-preview.1',
        route_values=route_values)