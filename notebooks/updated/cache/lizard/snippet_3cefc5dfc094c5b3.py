def reload_module(self, module_path=None):
    if module_path is None:
        if self.current_module is not None:
            module_path = self.current_module.name
        else:
            self.logger.warning(
                'must specify module if not module is currently being used')
            return False
    if module_path not in self.module:
        self.logger.error('invalid module requested for reload')
        raise termineter.errors.FrameworkRuntimeError(
            'invalid module requested for reload')
    self.logger.info('reloading module: ' + module_path)
    module_instance = self.import_module(module_path, reload_module=True)
    if not isinstance(module_instance, termineter.module.TermineterModule):
        self.logger.error('module: ' + module_path +
            ' is not derived from the TermineterModule class')
        raise termineter.errors.FrameworkRuntimeError('module: ' +
            module_path + ' is not derived from the TermineterModule class')
    if not hasattr(module_instance, 'run'):
        self.logger.error('module: ' + module_path + ' has no run() method')
        raise termineter.errors.FrameworkRuntimeError('module: ' +
            module_path + ' has no run() method')
    if not isinstance(module_instance.options, termineter.options.Options
        ) or not isinstance(module_instance.advanced_options, termineter.
        options.Options):
        self.logger.error('module: ' + module_path +
            ' options and advanced_options must be termineter.options.Options instances'
            )
        raise termineter.errors.FrameworkRuntimeError(
            'options and advanced_options must be termineter.options.Options instances'
            )
    module_instance.name = module_path.split('/')[-1]
    module_instance.path = module_path
    self.modules[module_path] = module_instance
    if self.current_module is not None:
        if self.current_module.path == module_instance.path:
            self.current_module = module_instance
    return True