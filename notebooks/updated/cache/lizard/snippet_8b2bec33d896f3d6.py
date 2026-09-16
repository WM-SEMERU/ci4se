def get_assessment_part_item_session(self, *args, **kwargs):
    if not self.supports_assessment_part_lookup():
        raise errors.Unimplemented()
    if self._proxy_in_args(*args, **kwargs):
        raise errors.InvalidArgument(
            'A Proxy object was received but not expected.')
    return sessions.AssessmentPartItemSession(runtime=self._runtime)