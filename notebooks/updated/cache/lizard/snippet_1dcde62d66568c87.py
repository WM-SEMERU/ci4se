def normalize(ctx, text):
    if text:
        click.echo(ctx.obj['cucco'].normalize(text))
    else:
        for line in sys.stdin:
            click.echo(ctx.obj['cucco'].normalize(line))