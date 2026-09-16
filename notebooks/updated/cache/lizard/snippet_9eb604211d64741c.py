def get_module(self, name, folder=None):
    pymod = self.pycore.builtin_module(name)
    if pymod is not None:
        return pymod
    module = self.find_module(name, folder)
    if module is None:
        raise ModuleNotFoundError('Module %s not found' % name)
    return self.pycore.resource_to_pyobject(module)