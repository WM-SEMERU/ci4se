def create_profile(self, parent, profile, retry=google.api_core.gapic_v1.
    method.DEFAULT, timeout=google.api_core.gapic_v1.method.DEFAULT,
    metadata=None):
    if 'create_profile' not in self._inner_api_calls:
        self._inner_api_calls['create_profile'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_profile, default_retry=self._method_configs[
            'CreateProfile'].retry, default_timeout=self._method_configs[
            'CreateProfile'].timeout, client_info=self._client_info)
    request = profile_service_pb2.CreateProfileRequest(parent=parent,
        profile=profile)
    return self._inner_api_calls['create_profile'](request, retry=retry,
        timeout=timeout, metadata=metadata)