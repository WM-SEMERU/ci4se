def import_module(self, module):
    if self.remote_import_system is not None:
        if self.remote_import_system == 'json':
            self.remote_module = JsonModuleExecute(self, module, self.logger)
        else:
            self.remote_module = LegacyModuleExecute(self.gateway, module,
                self.logger)
    else:
        self.remote_module = LegacyModuleExecute(self.gateway, module, self
            .logger)
    return self.remote_module