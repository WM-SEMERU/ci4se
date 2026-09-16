def _format_envvars(ctx):
    params = [x for x in ctx.command.params if getattr(x, 'envvar')]
    for param in params:
        yield '.. _{command_name}-{param_name}-{envvar}:'.format(command_name
            =ctx.command_path.replace(' ', '-'), param_name=param.name,
            envvar=param.envvar)
        yield ''
        for line in _format_envvar(param):
            yield line
        yield ''