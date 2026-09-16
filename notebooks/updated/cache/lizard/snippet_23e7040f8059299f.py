def config(commands=None, config_file=None, template_engine='jinja',
    context=None, defaults=None, saltenv='base', **kwargs):
    initial_config = show('show running-config', **kwargs)[0]
    if config_file:
        file_str = __salt__['cp.get_file_str'](config_file, saltenv=saltenv)
        if file_str is False:
            raise CommandExecutionError('Source file {} not found'.format(
                config_file))
    elif commands:
        if isinstance(commands, (six.string_types, six.text_type)):
            commands = [commands]
        file_str = '\n'.join(commands)
    if template_engine:
        file_str = __salt__['file.apply_template_on_contents'](file_str,
            template_engine, context, defaults, saltenv)
    commands = [line for line in file_str.splitlines() if line.strip()]
    ret = _cli_command(commands, **kwargs)
    current_config = show('show running-config', **kwargs)[0]
    diff = difflib.unified_diff(initial_config.splitlines(1)[4:],
        current_config.splitlines(1)[4:])
    return ''.join([x.replace('\r', '') for x in diff])