def _loadViperServices(self):
    servicesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'service')
    for serviceFile in os.listdir(servicesPath):
        if serviceFile.startswith('__') or serviceFile.startswith('.'):
            continue
        serviceName = serviceFile.replace('.py', '')
        servicePath = os.path.join(servicesPath, serviceFile)
        if not os.path.isfile(servicePath):
            continue
        serviceSpec = importlib.util.spec_from_file_location(serviceName,
            servicePath)
        service = importlib.util.module_from_spec(serviceSpec)
        serviceSpec.loader.exec_module(service)
        serviceInstance = service.Service(self)
        self.addService('viper', serviceName, serviceInstance)