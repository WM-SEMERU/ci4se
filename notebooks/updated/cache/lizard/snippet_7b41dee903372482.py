def set_access_control_lists(self, access_control_lists, security_namespace_id
    ):
    route_values = {}
    if security_namespace_id is not None:
        route_values['securityNamespaceId'] = self._serialize.url(
            'security_namespace_id', security_namespace_id, 'str')
    content = self._serialize.body(access_control_lists,
        'VssJsonCollectionWrapper')
    self._send(http_method='POST', location_id=
        '18a2ad18-7571-46ae-bec7-0c7da1495885', version='5.0', route_values
        =route_values, content=content)