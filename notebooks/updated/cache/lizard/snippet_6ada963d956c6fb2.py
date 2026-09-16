def list():
    entries = lambder.list_events()
    for e in entries:
        click.echo(str(e))