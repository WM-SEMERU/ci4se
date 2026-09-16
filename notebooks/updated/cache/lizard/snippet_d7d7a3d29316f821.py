def config_hook(self, func):
    argspec = inspect.getargspec(func)
    args = ['config', 'command_name', 'logger']
    if not (argspec.args == args and argspec.varargs is None and argspec.
        keywords is None and argspec.defaults is None):
        raise ValueError(
            'Wrong signature for config_hook. Expected: (config, command_name, logger)'
            )
    self.config_hooks.append(func)
    return self.config_hooks[-1]