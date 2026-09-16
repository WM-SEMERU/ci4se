def uninstall(ctx, yes, services):
    logger.debug('running command %s (%s)', ctx.command.name, ctx.params,
        extra={'command': ctx.command.name, 'params': ctx.params})
    home = ctx.obj['HOME']
    for service in services:
        service_path = plugin_utils.get_plugin_path(home, SERVICES, service)
        plugin_utils.uninstall_plugin(service_path, yes)