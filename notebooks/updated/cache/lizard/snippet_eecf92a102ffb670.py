def permission_to_pyramid_acls(permissions):
    acls = []
    for perm in permissions:
        if perm.type == 'user':
            acls.append((Allow, perm.user.id, perm.perm_name))
        elif perm.type == 'group':
            acls.append((Allow, 'group:%s' % perm.group.id, perm.perm_name))
    return acls