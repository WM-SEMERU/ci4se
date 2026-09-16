def config(config, skip_defaults):
    configurator = ClickConfigurator(vodka.plugin, skip_defaults=skip_defaults)
    configurator.configure(vodka.config.instance, vodka.config.InstanceHandler)
    try:
        dst = munge_config.parse_url(config)
    except ValueError:
        config = os.path.join(config, 'config.yaml')
        dst = munge_config.parse_url(config)
    config_dir = os.path.dirname(config)
    if not os.path.exists(config_dir) and config_dir:
        os.makedirs(config_dir)
    dst.cls().dumpu(vodka.config.instance, dst.url.path)
    if configurator.action_required:
        click.echo('')
        click.echo(
            'not all required values could be set by this script, please manually edit the config and set the following values'
            )
        click.echo('')
        for item in configurator.action_required:
            click.echo('- %s' % item)
        click.echo('')
    click.echo('Config written to %s' % dst.url.path)