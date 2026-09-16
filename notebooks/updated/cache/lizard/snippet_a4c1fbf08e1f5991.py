def get_service(self, service_name):
    service = self.services.get(service_name)
    if not service:
        raise KeyError('Service not registered: %s' % service_name)
    return service