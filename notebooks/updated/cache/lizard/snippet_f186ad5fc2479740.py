def is_permitted(self, permission_s):
    if self.authorized:
        self.check_security_manager()
        return self.security_manager.is_permitted(self.identifiers,
            permission_s)
    msg = (
        "Cannot check permission when user isn't authenticated nor remembered")
    raise ValueError(msg)