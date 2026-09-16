def get_objective_admin_session(self):
    if not self.supports_objective_admin():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise OperationFailed()
    try:
        session = sessions.ObjectiveAdminSession(runtime=self._runtime)
    except AttributeError:
        raise OperationFailed()
    return session