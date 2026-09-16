def from_dict(cls, acl_dict):
    perms = acl_dict.get('perms', Permissions.ALL)
    id_dict = acl_dict.get('id', {})
    id_scheme = id_dict.get('scheme', 'world')
    id_id = id_dict.get('id', 'anyone')
    return ACL(perms, Id(id_scheme, id_id))