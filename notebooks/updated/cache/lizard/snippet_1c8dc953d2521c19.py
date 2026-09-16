def import_product_sets(self, parent, input_config, retry=google.api_core.
    gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.method.
    DEFAULT, metadata=None):
    if 'import_product_sets' not in self._inner_api_calls:
        self._inner_api_calls['import_product_sets'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            import_product_sets, default_retry=self._method_configs[
            'ImportProductSets'].retry, default_timeout=self.
            _method_configs['ImportProductSets'].timeout, client_info=self.
            _client_info)
    request = product_search_service_pb2.ImportProductSetsRequest(parent=
        parent, input_config=input_config)
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
    operation = self._inner_api_calls['import_product_sets'](request, retry
        =retry, timeout=timeout, metadata=metadata)
    return google.api_core.operation.from_gapic(operation, self.transport.
        _operations_client, product_search_service_pb2.
        ImportProductSetsResponse, metadata_type=product_search_service_pb2
        .BatchOperationMetadata)