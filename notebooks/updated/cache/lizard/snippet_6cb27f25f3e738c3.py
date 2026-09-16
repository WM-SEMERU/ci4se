def from_acl_response(acl_response):
    if 'read' in acl_response:
        read_acl = AclType.from_acl_response(acl_response['read'])
        return Acl(read_acl)
    else:
        raise ValueError('Response does not contain read ACL')