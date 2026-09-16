def get_requested_third_party_permissions(self):
    third_party_permissions = []
    all_permissions = self.get_permissions()
    for perm in all_permissions:
        if perm not in list(self.permission_module.keys()):
            third_party_permissions.append(perm)
    return third_party_permissions