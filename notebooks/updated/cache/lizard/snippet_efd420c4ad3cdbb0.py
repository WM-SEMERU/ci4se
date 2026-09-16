def use_federated_objective_bank_view(self):
    self._objective_bank_view = FEDERATED
    for session in self._get_provider_sessions():
        try:
            session.use_federated_objective_bank_view()
        except AttributeError:
            pass