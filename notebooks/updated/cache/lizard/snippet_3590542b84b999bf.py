def get_assessment_results_session_for_bank(self, bank_id, proxy):
    if not self.supports_assessment_results():
        raise errors.Unimplemented()
    return sessions.AssessmentResultsSession(bank_id, proxy, self._runtime)