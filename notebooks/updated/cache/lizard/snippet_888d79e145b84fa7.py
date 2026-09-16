def call_api(self, resource_path, method, path_params=None, query_params=
    None, header_params=None, body=None, post_params=None, files=None,
    response_type=None, auth_settings=None, callback=None,
    _return_http_data_only=None, collection_formats=None, _preload_content=
    True, _request_timeout=None):
    if callback is None:
        return self.__call_api(resource_path, method, path_params,
            query_params, header_params, body, post_params, files,
            response_type, auth_settings, callback, _return_http_data_only,
            collection_formats, _preload_content, _request_timeout)
    else:
        thread = threading.Thread(target=self.__call_api, args=(
            resource_path, method, path_params, query_params, header_params,
            body, post_params, files, response_type, auth_settings,
            callback, _return_http_data_only, collection_formats,
            _preload_content, _request_timeout))
    thread.start()
    return thread