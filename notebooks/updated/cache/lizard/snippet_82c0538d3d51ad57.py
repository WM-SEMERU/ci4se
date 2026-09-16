def setup(self):
    for conf_name in self.py3_config['i3s_modules']:
        module = I3statusModule(conf_name, self)
        self.i3modules[conf_name] = module
        if module.is_time_module:
            self.time_modules.append(module)