def snaql_migration(ctx, db_uri, migrations, app, config):
    if config:
        migrations_config = _parse_config(config)
    elif db_uri and migrations and app:
        migrations_config = _generate_config(db_uri, migrations, app)
    else:
        raise click.ClickException(
            'If --config is not set, then --db-uri, --migrations and --app must be provided'
            )
    ctx.obj = {'config': migrations_config}
    try:
        ctx.obj['db'] = DBWrapper(ctx.obj['config']['db_uri'])
    except Exception as e:
        raise click.ClickException(
            'Unable to connect to database, exception is "{0}"'.format(str(e)))