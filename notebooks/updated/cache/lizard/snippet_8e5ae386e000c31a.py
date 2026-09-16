def use_comparative_objective_bank_view(self):
    self._objective_bank_view = COMPARATIVE
    for session in self._get_provider_sessions():
        try:
            session.use_comparative_objective_bank_view()
        except AttributeError:
            pass