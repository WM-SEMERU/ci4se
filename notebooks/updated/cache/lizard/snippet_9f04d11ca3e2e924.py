def get_activity_admin_session(self, proxy):
    if not self.supports_activity_admin():
        raise errors.Unimplemented()
    return sessions.ActivityAdminSession(proxy=proxy, runtime=self._runtime)