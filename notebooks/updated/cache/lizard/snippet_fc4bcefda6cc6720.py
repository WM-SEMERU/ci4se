def add_role(self, databaseName, roleName, collectionName=None):
    role = {'databaseName': databaseName, 'roleName': roleName}
    if collectionName:
        role['collectionName'] = collectionName
    if collectionName and roleName not in [RoleSpecs.read, RoleSpecs.readWrite
        ]:
        raise ErrRole('Permissions [%s] not available for a collection' %
            roleName)
    elif not collectionName and roleName not in [RoleSpecs.read, RoleSpecs.
        readWrite, RoleSpecs.dbAdmin] and databaseName != 'admin':
        raise ErrRole(
            'Permissions [%s] is only available for admin database' % roleName)
    if role not in self.roles:
        self.roles.append(role)