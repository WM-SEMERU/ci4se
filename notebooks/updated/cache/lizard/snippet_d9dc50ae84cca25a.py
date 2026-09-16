def validate_access_permission(self, valid_permissions):
    self.check_connection()
    if typepy.is_null_string(self.mode):
        raise ValueError('mode is not set')
    if self.mode not in valid_permissions:
        raise IOError("invalid access: expected-mode='{}', current-mode='{}'"
            .format("' or '".join(valid_permissions), self.mode))