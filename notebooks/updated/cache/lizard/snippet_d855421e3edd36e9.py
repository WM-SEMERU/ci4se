def revoke_user_access(self, instance, user, db_names, strict=True):
    return instance.revoke_user_access(user, db_names, strict=strict)