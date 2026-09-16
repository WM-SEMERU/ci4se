def use_isolated_bin_view(self):
    self._bin_view = ISOLATED
    for session in self._get_provider_sessions():
        try:
            session.use_isolated_bin_view()
        except AttributeError:
            pass