def check_membership_existence(self, subject_descriptor, container_descriptor):
    route_values = {}
    if subject_descriptor is not None:
        route_values['subjectDescriptor'] = self._serialize.url(
            'subject_descriptor', subject_descriptor, 'str')
    if container_descriptor is not None:
        route_values['containerDescriptor'] = self._serialize.url(
            'container_descriptor', container_descriptor, 'str')
    self._send(http_method='HEAD', location_id=
        '3fd2e6ca-fb30-443a-b579-95b19ed0934c', version='5.1-preview.1',
        route_values=route_values)