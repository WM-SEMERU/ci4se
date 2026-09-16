def get_composition_repository_session(self, proxy):
    if not self.supports_composition_repository():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise
    proxy = self._convert_proxy(proxy)
    try:
        session = sessions.CompositionRepositorySession(proxy, runtime=self
            ._runtime)
    except AttributeError:
        raise
    return session