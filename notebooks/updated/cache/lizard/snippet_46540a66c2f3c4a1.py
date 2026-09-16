def config(show, reset, **params):
    sh_config = SHConfig()
    if reset:
        sh_config.reset()
    for param, value in params.items():
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
            if getattr(sh_config, param) != value:
                setattr(sh_config, param, value)
    old_config = SHConfig()
    sh_config.save()
    for param in sh_config.get_params():
        if sh_config[param] != old_config[param]:
            value = sh_config[param]
            if isinstance(value, str):
                value = "'{}'".format(value)
            click.echo("The value of parameter '{}' was updated to {}".
                format(param, value))
    if show:
        click.echo(str(sh_config))
        click.echo('Configuration file location: {}'.format(sh_config.
            get_config_location()))