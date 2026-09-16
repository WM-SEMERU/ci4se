def _getModules(self):
    modules = {}
    modulesPath = os.path.join('application', 'module')
    moduleList = os.listdir(modulesPath)
    for moduleName in moduleList:
        modulePath = os.path.join(modulesPath, moduleName, 'module.py')
        if not os.path.isfile(modulePath):
            continue
        moduleSpec = importlib.util.spec_from_file_location(moduleName,
            modulePath)
        module = importlib.util.module_from_spec(moduleSpec)
        moduleSpec.loader.exec_module(module)
        moduleInstance = module.Module(self)
        modules[moduleName] = moduleInstance
    return modules