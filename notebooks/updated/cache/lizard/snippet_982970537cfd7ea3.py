def get_composition_admin_session_for_repository(self, repository_id=None):
    if repository_id is None:
        raise NullArgument()
    if not self.supports_composition_admin(
        ) or not self.supports_visible_federation():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise
    try:
        session = sessions.CompositionSearchSession(repository_id, proxy=
            self._proxy, runtime=self._runtime)
    except AttributeError:
        raise
    return session