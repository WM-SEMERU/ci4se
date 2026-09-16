def use_unsequestered_assessment_part_view(self):
    self._containable_views['assessment_part'] = UNSEQUESTERED
    self._get_sub_package_provider_session('assessment_authoring',
        'assessment_part_lookup_session')
    for session in self._provider_sessions:
        for provider_session_name, provider_session in self._provider_sessions[
            session].items():
            try:
                provider_session.use_unsequestered_assessment_part_view()
            except AttributeError:
                pass