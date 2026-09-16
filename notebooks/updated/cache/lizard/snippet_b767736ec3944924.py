def get_update(self, id, update_number, project=None):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if id is not None:
        route_values['id'] = self._serialize.url('id', id, 'int')
    if update_number is not None:
        route_values['updateNumber'] = self._serialize.url('update_number',
            update_number, 'int')
    response = self._send(http_method='GET', location_id=
        '6570bf97-d02c-4a91-8d93-3abe9895b1a9', version='5.1-preview.3',
        route_values=route_values)
    return self._deserialize('WorkItemUpdate', response)