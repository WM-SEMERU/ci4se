def get_rubric(self):
    if not bool(self._my_map['rubricId']):
        raise errors.IllegalState('this AssessmentOffered has no rubric')
    mgr = self._get_provider_manager('ASSESSMENT')
    if not mgr.supports_assessment_offered_lookup():
        raise errors.OperationFailed(
            'Assessment does not support AssessmentOffered lookup')
    lookup_session = mgr.get_assessment_offered_lookup_session(proxy=
        getattr(self, '_proxy', None))
    lookup_session.use_federated_bank_view()
    osid_object = lookup_session.get_assessment_offered(self.get_rubric_id())
    return osid_object