def invoke(cls, ns, banner):
    try:
        from IPython.frontend.terminal.embed import InteractiveShellEmbed
        from IPython.frontend.terminal.ipapp import load_default_config
        config = load_default_config()
        shell = InteractiveShellEmbed(config=config, banner2=banner)
        shell(local_ns=ns)
    except ImportError:
        from IPython.Shell import IPShellEmbed
        shell = IPShellEmbed(argv=[])
        shell.set_banner(shell.IP.BANNER + '\n\n' + banner)
        shell(local_ns=ns, global_ns={})