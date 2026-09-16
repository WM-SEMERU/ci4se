def get_proficiency_search_session(self, proxy):
    if not self.supports_proficiency_search():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise OperationFailed()
    proxy = self._convert_proxy(proxy)
    try:
        session = sessions.ProficiencySearchSession(proxy=proxy, runtime=
            self._runtime)
    except AttributeError:
        raise OperationFailed()
    return session