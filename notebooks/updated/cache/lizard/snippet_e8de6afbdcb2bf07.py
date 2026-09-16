def access_storage_rm(name, yes, **kwargs):
    if name is None:
        if not yes:
            click.confirm('Are you sure you want to remove all ACL?', abort
                =True)
    ctx = Context(**kwargs)
    ctx.execute_action('access:storage:rm', **{'storage': ctx.repo.
        create_secure_service('storage'), 'name': name})