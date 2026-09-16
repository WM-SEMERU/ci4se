def profile_remove(name, **kwargs):
    ctx = Context(**kwargs)
    ctx.execute_action('profile:remove', **{'storage': ctx.repo.
        create_secure_service('storage'), 'name': name})