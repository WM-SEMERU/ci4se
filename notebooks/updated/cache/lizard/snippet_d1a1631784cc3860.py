def has_perm(self, perm, obj, check_groups=True, approved=True):
    if self.user:
        if self.has_user_perms(perm, obj, approved, check_groups):
            return True
    if self.group:
        return self.has_group_perms(perm, obj, approved)
    return False