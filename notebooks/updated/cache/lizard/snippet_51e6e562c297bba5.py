def update_security_marks(self, security_marks, update_mask=None,
    start_time=None, retry=google.api_core.gapic_v1.method.DEFAULT, timeout
    =google.api_core.gapic_v1.method.DEFAULT, metadata=None):
    if 'update_security_marks' not in self._inner_api_calls:
        self._inner_api_calls['update_security_marks'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            update_security_marks, default_retry=self._method_configs[
            'UpdateSecurityMarks'].retry, default_timeout=self.
            _method_configs['UpdateSecurityMarks'].timeout, client_info=
            self._client_info)
    request = securitycenter_service_pb2.UpdateSecurityMarksRequest(
        security_marks=security_marks, update_mask=update_mask, start_time=
        start_time)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('security_marks.name', security_marks.name)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    return self._inner_api_calls['update_security_marks'](request, retry=
        retry, timeout=timeout, metadata=metadata)