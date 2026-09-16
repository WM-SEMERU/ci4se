def keyring_update(cid, **kwargs):
    ctx = Context(**kwargs)
    ctx.execute_action('keyring:update', **{'tvm': ctx.repo.
        create_secure_service('tvm'), 'cid': cid})