def create_session(self, database, session=None, retry=google.api_core.
    gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.method.
    DEFAULT, metadata=None):
    if 'create_session' not in self._inner_api_calls:
        self._inner_api_calls['create_session'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_session, default_retry=self._method_configs[
            'CreateSession'].retry, default_timeout=self._method_configs[
            'CreateSession'].timeout, client_info=self._client_info)
    request = spanner_pb2.CreateSessionRequest(database=database, session=
        session)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('database', database)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    return self._inner_api_calls['create_session'](request, retry=retry,
        timeout=timeout, metadata=metadata)