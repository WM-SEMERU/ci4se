def generate_identity_binding_access_token(self, name, scope, jwt, retry=
    google.api_core.gapic_v1.method.DEFAULT, timeout=google.api_core.
    gapic_v1.method.DEFAULT, metadata=None):
    if 'generate_identity_binding_access_token' not in self._inner_api_calls:
        self._inner_api_calls['generate_identity_binding_access_token'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            generate_identity_binding_access_token, default_retry=self.
            _method_configs['GenerateIdentityBindingAccessToken'].retry,
            default_timeout=self._method_configs[
            'GenerateIdentityBindingAccessToken'].timeout, client_info=self
            ._client_info)
    request = common_pb2.GenerateIdentityBindingAccessTokenRequest(name=
        name, scope=scope, jwt=jwt)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('name', name)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    return self._inner_api_calls['generate_identity_binding_access_token'](
        request, retry=retry, timeout=timeout, metadata=metadata)