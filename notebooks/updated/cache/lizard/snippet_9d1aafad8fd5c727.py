def _getInterfaces(self):
    interfaces = {}
    interfacesPath = os.path.join('application', 'interface')
    interfaceList = os.listdir(interfacesPath)
    for file in interfaceList:
        interfaceDirectoryPath = os.path.join(interfacesPath, file)
        if not os.path.isdir(interfaceDirectoryPath) or file.startswith('__'
            ) or file.startswith('.'):
            continue
        interfaceName = ntpath.basename(interfaceDirectoryPath)
        interfacePath = os.path.join(interfaceDirectoryPath, interfaceName
            ) + '.py'
        if not os.path.isfile(interfacePath):
            continue
        interfaceSpec = importlib.util.spec_from_file_location(interfaceName,
            interfacePath)
        interface = importlib.util.module_from_spec(interfaceSpec)
        interfaceSpec.loader.exec_module(interface)
        if hasattr(interface, 'Service'):
            interfaceInstance = interface.Service(self)
            interfaces[interfaceName] = interfaceInstance
    return interfaces