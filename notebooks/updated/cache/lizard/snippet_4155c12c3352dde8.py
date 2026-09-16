def print_table(*args, **kwargs):
    t = format_table(*args, **kwargs)
    click.echo(t)