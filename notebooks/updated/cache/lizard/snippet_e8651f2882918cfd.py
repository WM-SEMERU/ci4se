def async_batch_annotate_files(self, requests, retry=google.api_core.
    gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.method.
    DEFAULT, metadata=None):
    if 'async_batch_annotate_files' not in self._inner_api_calls:
        self._inner_api_calls['async_batch_annotate_files'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            async_batch_annotate_files, default_retry=self._method_configs[
            'AsyncBatchAnnotateFiles'].retry, default_timeout=self.
            _method_configs['AsyncBatchAnnotateFiles'].timeout, client_info
            =self._client_info)
    request = image_annotator_pb2.AsyncBatchAnnotateFilesRequest(requests=
        requests)
    operation = self._inner_api_calls['async_batch_annotate_files'](request,
        retry=retry, timeout=timeout, metadata=metadata)
    return google.api_core.operation.from_gapic(operation, self.transport.
        _operations_client, image_annotator_pb2.
        AsyncBatchAnnotateFilesResponse, metadata_type=image_annotator_pb2.
        OperationMetadata)