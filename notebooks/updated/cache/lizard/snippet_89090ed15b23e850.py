def get_instantiated_service(self, name):
    if name not in self.instantiated_services:
        raise UninstantiatedServiceException
    return self.instantiated_services[name]