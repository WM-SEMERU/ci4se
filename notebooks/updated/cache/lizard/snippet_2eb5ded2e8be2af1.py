def is_logon(self, verify=False):
    if self._session_id is None:
        return False
    if verify:
        try:
            self.get('/api/console', logon_required=True)
        except ServerAuthError:
            return False
    return True