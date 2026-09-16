def embed(**kwargs):
    config = kwargs.get('config')
    header = kwargs.pop('header', '')
    compile_flags = kwargs.pop('compile_flags', None)
    if config is None:
        config = load_default_config()
        config.InteractiveShellEmbed = config.TerminalInteractiveShell
        kwargs['config'] = config
    shell = InteractiveShellEmbed.instance(**kwargs)
    initialize_extensions(shell, config['InteractiveShellApp']['extensions'])
    shell(header=header, stack_depth=2, compile_flags=compile_flags)