def is_session_storage_enabled(self, subject=None):
    if subject.get_session(False):
        return True
    if not self.session_storage_enabled:
        return False
    if not hasattr(subject, 'web_registry'
        ) and self.session_manager and not isinstance(self.session_manager,
        session_abcs.NativeSessionManager):
        return False
    return subject.web_registry.session_creation_enabled