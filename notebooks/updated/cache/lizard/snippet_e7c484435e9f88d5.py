def create_finding(self, parent, finding_id, finding, retry=google.api_core
    .gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.method.
    DEFAULT, metadata=None):
    if 'create_finding' not in self._inner_api_calls:
        self._inner_api_calls['create_finding'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_finding, default_retry=self._method_configs[
            'CreateFinding'].retry, default_timeout=self._method_configs[
            'CreateFinding'].timeout, client_info=self._client_info)
    request = securitycenter_service_pb2.CreateFindingRequest(parent=parent,
        finding_id=finding_id, finding=finding)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('parent', parent)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    return self._inner_api_calls['create_finding'](request, retry=retry,
        timeout=timeout, metadata=metadata)