def delete_service_definition(self, service_type, identifier):
    route_values = {}
    if service_type is not None:
        route_values['serviceType'] = self._serialize.url('service_type',
            service_type, 'str')
    if identifier is not None:
        route_values['identifier'] = self._serialize.url('identifier',
            identifier, 'str')
    self._send(http_method='DELETE', location_id=
        'd810a47d-f4f4-4a62-a03f-fa1860585c4c', version='5.0-preview.1',
        route_values=route_values)