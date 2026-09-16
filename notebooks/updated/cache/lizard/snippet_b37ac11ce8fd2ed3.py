def drop_row_range(self, name, row_key_prefix=None,
    delete_all_data_from_table=None, retry=google.api_core.gapic_v1.method.
    DEFAULT, timeout=google.api_core.gapic_v1.method.DEFAULT, metadata=None):
    if 'drop_row_range' not in self._inner_api_calls:
        self._inner_api_calls['drop_row_range'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            drop_row_range, default_retry=self._method_configs[
            'DropRowRange'].retry, default_timeout=self._method_configs[
            'DropRowRange'].timeout, client_info=self._client_info)
    google.api_core.protobuf_helpers.check_oneof(row_key_prefix=
        row_key_prefix, delete_all_data_from_table=delete_all_data_from_table)
    request = bigtable_table_admin_pb2.DropRowRangeRequest(name=name,
        row_key_prefix=row_key_prefix, delete_all_data_from_table=
        delete_all_data_from_table)
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
    self._inner_api_calls['drop_row_range'](request, retry=retry, timeout=
        timeout, metadata=metadata)