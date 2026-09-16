def get_object_by_uid(uid, default=_marker):
    if not uid:
        if default is not _marker:
            return default
        fail('get_object_by_uid requires UID as first argument; got {} instead'
            .format(uid))
    if uid == '0':
        return get_portal()
    pc = get_portal_catalog()
    uc = get_tool('uid_catalog')
    brains = uc(UID=uid)
    if brains:
        return brains[0].getObject()
    res = pc(UID=uid)
    if not res:
        if default is not _marker:
            return default
        fail('No object found for UID {}'.format(uid))
    return get_object(res[0])