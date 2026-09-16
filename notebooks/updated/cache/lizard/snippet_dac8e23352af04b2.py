def ensure_path(path, acls=None, profile=None, hosts=None, scheme=None,
    username=None, password=None, default_acl=None):
    if acls is None:
        acls = []
    acls = [make_digest_acl(**acl) for acl in acls]
    conn = _get_zk_conn(profile=profile, hosts=hosts, scheme=scheme,
        username=username, password=password, default_acl=default_acl)
    return conn.ensure_path(path, acls)