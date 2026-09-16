def run_command(self, command_name, config_updates=None, named_configs=(),
    args=(), meta_info=None):
    import warnings
    warnings.warn('run_command is deprecated. Use run instead',
        DeprecationWarning)
    return self.run(command_name, config_updates, named_configs, meta_info,
        args)