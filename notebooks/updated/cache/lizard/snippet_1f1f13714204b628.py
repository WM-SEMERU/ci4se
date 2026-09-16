def workflow(ctx, client):
    if ctx.invoked_subcommand is None:
        from renku.models.refs import LinkReference
        names = defaultdict(list)
        for ref in LinkReference.iter_items(client, common_path='workflows'):
            names[ref.reference.name].append(ref.name)
        for path in client.workflow_path.glob('*.cwl'):
            click.echo('{path}: {names}'.format(path=path.name, names=', '.
                join(click.style(_deref(name), fg='green') for name in
                names[path.name])))