def cli(ctx, verbose, fake, install, uninstall, config):
    ctx.obj = SCMRepo()
    ctx.obj.fake = fake
    ctx.obj.verbose = fake or verbose
    if install:
        do_install(ctx, verbose, fake)
        ctx.exit()
    elif uninstall:
        do_uninstall(ctx, verbose, fake)
        ctx.exit()
    elif config:
        do_edit_settings(fake)
        ctx.exit()
    elif ctx.invoked_subcommand is None:
        click.echo(format_help(ctx.get_help()))