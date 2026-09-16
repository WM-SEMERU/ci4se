def delete_group(self, group_id):
    route_values = {}
    if group_id is not None:
        route_values['groupId'] = self._serialize.url('group_id', group_id,
            'str')
    self._send(http_method='DELETE', location_id=
        '5966283b-4196-4d57-9211-1b68f41ec1c2', version='5.0', route_values
        =route_values)