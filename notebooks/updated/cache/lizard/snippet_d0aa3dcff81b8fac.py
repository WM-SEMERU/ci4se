def _indexable_roles_and_users(self):
    from abilian.services.indexing import indexable_role
    from abilian.services.security import READ, Admin, Anonymous, Creator, Owner
    from abilian.services import get_service
    result = []
    security = get_service('security')
    assignments = security.get_permissions_assignments(permission=READ, obj
        =self)
    allowed_roles = assignments.get(READ, set())
    allowed_roles.add(Admin)
    for r in allowed_roles:
        result.append(indexable_role(r))
    for role, attr in ((Creator, 'creator'), (Owner, 'owner')):
        if role in allowed_roles:
            user = getattr(self, attr)
            if user:
                result.append(indexable_role(user))
    principals = set()
    for user, role in security.get_role_assignements(self):
        if role in allowed_roles:
            principals.add(user)
    if Anonymous in principals:
        principals.remove(Anonymous)
    for p in principals:
        result.append(indexable_role(p))
    return ' '.join(result)