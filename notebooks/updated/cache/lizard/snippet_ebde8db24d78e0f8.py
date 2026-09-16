def access_grant(tp, name, cid, uid, perm, **kwargs):
    ctx = Context(**kwargs)
    ctx.execute_action('access:edit:grant', **{'unicat': ctx.repo.
        create_secure_service('unicat'), 'tp': tp, 'name': name, 'cids':
        cid, 'uids': uid, 'perm': perm})