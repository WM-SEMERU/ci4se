def common_cli_config_options(f):

    @click.option('-C', '--config-file', envvar='CLOUDSMITH_CONFIG_FILE',
        type=click.Path(dir_okay=True, exists=True, writable=False,
        resolve_path=True), help='The path to your config.ini file.')
    @click.option('--credentials-file', envvar=
        'CLOUDSMITH_CREDENTIALS_FILE', type=click.Path(dir_okay=True,
        exists=True, writable=False, resolve_path=True), help=
        'The path to your credentials.ini file.')
    @click.option('-P', '--profile', default=None, envvar=
        'CLOUDSMITH_PROFILE', help=
        'The name of the profile to use for configuration.')
    @click.pass_context
    @functools.wraps(f)
    def wrapper(ctx, *args, **kwargs):
        opts = config.get_or_create_options(ctx)
        profile = kwargs.pop('profile')
        config_file = kwargs.pop('config_file')
        creds_file = kwargs.pop('credentials_file')
        opts.load_config_file(path=config_file, profile=profile)
        opts.load_creds_file(path=creds_file, profile=profile)
        kwargs['opts'] = opts
        return ctx.invoke(f, *args, **kwargs)
    return wrapper