def set_perms(obj_name, obj_type='file', grant_perms=None, deny_perms=None,
    inheritance=True, reset=False):
    ret = {}
    if reset:
        obj_dacl = dacl(obj_type=obj_type)
        cur_perms = {}
    else:
        obj_dacl = dacl(obj_name, obj_type=obj_type)
        cur_perms = get_permissions(obj_name=obj_name, obj_type=obj_type)
    if deny_perms is not None:
        ret['deny'] = _set_perms(obj_dacl=obj_dacl, obj_type=obj_type,
            new_perms=deny_perms, cur_perms=cur_perms, access_mode='deny')
    if grant_perms is not None:
        ret['grant'] = _set_perms(obj_dacl=obj_dacl, obj_type=obj_type,
            new_perms=grant_perms, cur_perms=cur_perms, access_mode='grant')
    obj_dacl.order_acl()
    if obj_dacl.save(obj_name, not inheritance):
        return ret
    return {}