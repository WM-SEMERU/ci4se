def get_supported_languages(self, parent=None, display_language_code=None,
    model=None, retry=google.api_core.gapic_v1.method.DEFAULT, timeout=
    google.api_core.gapic_v1.method.DEFAULT, metadata=None):
    if 'get_supported_languages' not in self._inner_api_calls:
        self._inner_api_calls['get_supported_languages'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            get_supported_languages, default_retry=self._method_configs[
            'GetSupportedLanguages'].retry, default_timeout=self.
            _method_configs['GetSupportedLanguages'].timeout, client_info=
            self._client_info)
    request = translation_service_pb2.GetSupportedLanguagesRequest(parent=
        parent, display_language_code=display_language_code, model=model)
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
    return self._inner_api_calls['get_supported_languages'](request, retry=
        retry, timeout=timeout, metadata=metadata)