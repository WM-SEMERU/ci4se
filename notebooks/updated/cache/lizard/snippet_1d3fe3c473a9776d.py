def get_authorization_vault_assignment_session(self):
    if not self.supports_authorization_vault_assignment():
        raise errors.Unimplemented()
    return sessions.AuthorizationVaultAssignmentSession(runtime=self._runtime)