def revoke_user_access(self, user, db_names, strict=True):
    return self._user_manager.revoke_user_access(user, db_names, strict=strict)