def update(gandi, resource, memory, cores, console, password, background,
    reboot):
    pwd = None
    if password:
        pwd = click.prompt('password', hide_input=True, confirmation_prompt
            =True)
    max_memory = None
    if memory:
        max_memory = gandi.iaas.required_max_memory(resource, memory)
    if max_memory and not reboot:
        gandi.echo('memory update must be done offline.')
        if not click.confirm('reboot machine %s?' % resource):
            return
    result = gandi.iaas.update(resource, memory, cores, console, pwd,
        background, max_memory)
    if background:
        gandi.pretty_echo(result)
    return result