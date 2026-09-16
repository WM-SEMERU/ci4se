def use_active_sequence_rule_view(self):
    self._operable_views['sequence_rule'] = ACTIVE
    for session in self._get_provider_sessions():
        try:
            session.use_active_sequence_rule_view()
        except AttributeError:
            pass