def get_assessments_by_bank(self, bank_id):
    mgr = self._get_provider_manager('ASSESSMENT', local=True)
    lookup_session = mgr.get_assessment_lookup_session_for_bank(bank_id,
        proxy=self._proxy)
    lookup_session.use_isolated_bank_view()
    return lookup_session.get_assessments()