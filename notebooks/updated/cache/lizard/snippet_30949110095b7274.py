def auth_list(**kwargs):
    ctx = Context(**kwargs)
    ctx.execute_action('auth:group:list', **{'storage': ctx.repo.
        create_secure_service('storage')})