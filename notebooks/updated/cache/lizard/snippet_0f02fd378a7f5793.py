def _to_enos_roles(roles):

    def to_host(h):
        extra = {}
        for nic, roles in h['nics']:
            for role in roles:
                extra[role] = nic
        return Host(h['host'], user='root', extra=extra)
    enos_roles = {}
    for role, hosts in roles.items():
        enos_roles[role] = [to_host(h) for h in hosts]
    logger.debug(enos_roles)
    return enos_roles