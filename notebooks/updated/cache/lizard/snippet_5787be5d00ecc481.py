def unassign_assessment_from_bank(self, assessment_id, bank_id):
    mgr = self._get_provider_manager('ASSESSMENT', local=True)
    lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
    lookup_session.get_bank(bank_id)
    self._unassign_object_from_catalog(assessment_id, bank_id)