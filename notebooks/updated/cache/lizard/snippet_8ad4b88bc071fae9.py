def load_cli_plugins(cli, config_dir=None):
    from .config import load_master_config
    config = load_master_config(config_dir=config_dir)
    plugins = discover_plugins(config.Plugins.dirs)
    for plugin in plugins:
        if not hasattr(plugin, 'attach_to_cli'):
            continue
        logger.debug('Attach plugin `%s` to CLI.', _fullname(plugin))
        try:
            plugin().attach_to_cli(cli)
        except Exception as e:
            logger.error('Error when loading plugin `%s`: %s', plugin, e)