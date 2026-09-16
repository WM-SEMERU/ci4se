def get_assessment_offered_bank_session(self, proxy):
    if not self.supports_assessment_offered_bank():
        raise errors.Unimplemented()
    return sessions.AssessmentOfferedBankSession(proxy=proxy, runtime=self.
        _runtime)