def runlist_view(name, **kwargs):
    ctx = Context(**kwargs)
    ctx.execute_action('runlist:view', **{'storage': ctx.repo.
        create_secure_service('storage'), 'name': name})