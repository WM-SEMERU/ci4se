def save(self, *module_names):
    for modname in module_names:
        self._saved[modname] = sys.modules.get(modname, None)