def update_quota(tenant_id, subnet=None, router=None, network=None,
    floatingip=None, port=None, security_group=None, security_group_rule=
    None, profile=None):
    conn = _auth(profile)
    return conn.update_quota(tenant_id, subnet, router, network, floatingip,
        port, security_group, security_group_rule)