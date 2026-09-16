def endpoint(url):
    if not url:
        click.secho(dtool_config.utils.get_ecs_endpoint(CONFIG_PATH))
    else:
        click.secho(dtool_config.utils.set_ecs_endpoint(CONFIG_PATH, url))