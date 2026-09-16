def cli(obj):
    for k, v in obj.items():
        if isinstance(v, list):
            v = ', '.join(v)
        click.echo('{:20}: {}'.format(k, v))