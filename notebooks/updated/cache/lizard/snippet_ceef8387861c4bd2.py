def module2upstream(mod):
    for rule in OPENSTACK_UPSTREAM_PKG_MAP:
        pkglist = rule(mod, dist=None)
        if pkglist:
            return pkglist[0]
    return mod