def use_federated_vault_view(self):
    self._vault_view = FEDERATED
    for session in self._get_provider_sessions():
        try:
            session.use_federated_vault_view()
        except AttributeError:
            pass