def load_module(self, name):
    self.loaded_modules.append(name)
    try:
        __import__(name, {}, {}, [])
        mod = sys.modules[name]
        self._run_hooks(name, mod)
    except:
        self.loaded_modules.pop()
        raise
    return mod