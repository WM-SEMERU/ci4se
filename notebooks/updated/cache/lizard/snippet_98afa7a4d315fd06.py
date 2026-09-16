def cli(main, conf_dir=None, commands_dir=None):
    return Command(main, conf_dir=conf_dir, commands_dir=commands_dir)()