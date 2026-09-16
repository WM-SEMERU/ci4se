def unassign_proficiency_from_objective_bank(self, proficiency_id,
    objective_bank_id):
    mgr = self._get_provider_manager('LEARNING', local=True)
    lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
    lookup_session.get_objective_bank(objective_bank_id)
    self._unassign_object_from_catalog(proficiency_id, objective_bank_id)