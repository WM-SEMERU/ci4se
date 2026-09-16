def service(self, service):
    if service is None:
        raise ValueError('Invalid value for `service`, must not be `None`')
    allowed_values = ['lwm2m', 'bootstrap']
    if service not in allowed_values:
        raise ValueError(
            'Invalid value for `service` ({0}), must be one of {1}'.format(
            service, allowed_values))
    self._service = service