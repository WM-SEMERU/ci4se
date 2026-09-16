def get_roles(self):
    prefix = _IDENTITY_NS + _ROLE_NS
    rolelist_list = [_create_from_bytes(d, identity_pb2.RoleList) for _, d in
        self._state_view.leaves(prefix=prefix)]
    roles = []
    for role_list in rolelist_list:
        for role in role_list.roles:
            roles.append(role)
    return sorted(roles, key=lambda r: r.name)