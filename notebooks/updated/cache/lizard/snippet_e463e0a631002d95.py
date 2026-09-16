def run(ctx, args):
    if not args:
        click.echo(ctx.get_help())
        return
    with chdir(get_root()):
        result = run_command(args)
    ctx.exit(result.code)