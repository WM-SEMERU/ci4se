def register_module(self, module, idx=-1):
    if module in self._modules:
        raise AlreadyRegisteredError(
            "Module '{0}' is already registered on loader.".format(module))
    if idx < 0:
        self._modules.append(module)
    else:
        self._modules.insert(idx, module)