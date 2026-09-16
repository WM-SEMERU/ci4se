def get_assessment_query_session_for_bank(self, bank_id, proxy):
    if not self.supports_assessment_query():
        raise errors.Unimplemented()
    return sessions.AssessmentQuerySession(bank_id, proxy, self._runtime)