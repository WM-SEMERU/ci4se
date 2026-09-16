def update_service_definitions(self, service_definitions):
    content = self._serialize.body(service_definitions,
        'VssJsonCollectionWrapper')
    self._send(http_method='PATCH', location_id=
        'd810a47d-f4f4-4a62-a03f-fa1860585c4c', version='5.0-preview.1',
        content=content)