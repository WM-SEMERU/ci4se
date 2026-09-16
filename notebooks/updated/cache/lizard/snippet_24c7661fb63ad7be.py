def cli(obj, role, scopes, delete):
    client = obj['client']
    if delete:
        client.delete_perm(delete)
    else:
        if not role:
            raise click.UsageError('Missing option "--role".')
        if not scopes:
            raise click.UsageError('Missing option "--scope".')
        try:
            perm = client.create_perm(role, scopes)
        except Exception as e:
            click.echo('ERROR: {}'.format(e))
            sys.exit(1)
        click.echo(perm.id)