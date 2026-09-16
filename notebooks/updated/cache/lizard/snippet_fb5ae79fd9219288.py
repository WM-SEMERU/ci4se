def read_rows(self, table_name, app_profile_id=None, rows=None, filter_=
    None, rows_limit=None, retry=google.api_core.gapic_v1.method.DEFAULT,
    timeout=google.api_core.gapic_v1.method.DEFAULT, metadata=None):
    if 'read_rows' not in self._inner_api_calls:
        self._inner_api_calls['read_rows'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            read_rows, default_retry=self._method_configs['ReadRows'].retry,
            default_timeout=self._method_configs['ReadRows'].timeout,
            client_info=self._client_info)
    request = bigtable_pb2.ReadRowsRequest(table_name=table_name,
        app_profile_id=app_profile_id, rows=rows, filter=filter_,
        rows_limit=rows_limit)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('table_name', table_name)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    return self._inner_api_calls['read_rows'](request, retry=retry, timeout
        =timeout, metadata=metadata)