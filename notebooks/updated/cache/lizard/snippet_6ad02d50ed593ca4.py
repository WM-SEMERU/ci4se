def use_comparative_log_view(self):
    self._log_view = COMPARATIVE
    for session in self._get_provider_sessions():
        try:
            session.use_comparative_log_view()
        except AttributeError:
            pass