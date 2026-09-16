def get_assessment_bank_session(self, proxy):
    if not self.supports_assessment_bank():
        raise errors.Unimplemented()
    return sessions.AssessmentBankSession(proxy=proxy, runtime=self._runtime)