def get_permissions(self):
    permissions = set()
    permissions.update(self.resource_manager.get_permissions())
    for f in self.resource_manager.filters:
        permissions.update(f.get_permissions())
    for a in self.resource_manager.actions:
        permissions.update(a.get_permissions())
    return permissions