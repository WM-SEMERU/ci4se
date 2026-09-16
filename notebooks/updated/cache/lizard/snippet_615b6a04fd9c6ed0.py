def module_config(self, settings_module):
    assert hasattr(settings_module, '__file__'), 'settings must be a module'
    self.set_root_path(settings_module=settings_module)
    app_log.debug('Set root_path: %s', self.root_path)
    global settings
    self.update_settings(dict([(i, getattr(settings_module, i)) for i in
        dir(settings_module) if not i.startswith('_') and i == i.upper()]))
    settings._module = settings_module
    settings._app = self