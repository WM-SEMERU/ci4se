def chown(path, user=None, group=None, recursive=False):
    successful = True
    uid = -1
    gid = -1
    if user is not None:
        if isinstance(user, basestring_type):
            user = _ops_user(name=user)
        elif isinstance(user, numbers.Number):
            user = _ops_user(id=user)
        if isinstance(user, _ops_user):
            if user:
                uid = user.id
            else:
                log.error('chown: unable to get uid')
                successful = False
        else:
            successful = False
    if group is not None:
        if isinstance(group, basestring_type):
            group = _ops_group(name=group)
        elif isinstance(group, numbers.Number):
            group = _ops_group(id=group)
        if isinstance(group, _ops_group):
            if group:
                gid = group.id
            else:
                log.error('chown: unable to get gid')
                successful = False
        else:
            successful = False
    if not (uid == -1 and gid == -1):
        if recursive:
            for p in find(path, no_peek=True):
                successful = _chown(p, uid=uid, gid=gid) and successful
        else:
            successful = _chown(path, uid=uid, gid=gid)
    else:
        successful = False
    return successful