def use_comparative_sequence_rule_enabler_rule_view(self):
    self._object_views['sequence_rule_enabler_rule'] = COMPARATIVE
    for session in self._get_provider_sessions():
        try:
            session.use_comparative_sequence_rule_enabler_rule_view()
        except AttributeError:
            pass