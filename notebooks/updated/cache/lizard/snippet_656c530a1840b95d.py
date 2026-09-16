def add_files_via_url(self, dataset_key, files={}):
    file_requests = [_swagger.FileCreateOrUpdateRequest(name=file_name,
        source=_swagger.FileSourceCreateOrUpdateRequest(url=file_info['url'
        ], expand_archive=file_info.get('expand_archive', False)),
        description=file_info.get('description'), labels=file_info.get(
        'labels')) for file_name, file_info in files.items()]
    owner_id, dataset_id = parse_dataset_key(dataset_key)
    try:
        self._datasets_api.add_files_by_source(owner_id, dataset_id,
            _swagger.FileBatchUpdateRequest(files=file_requests))
    except _swagger.rest.ApiException as e:
        raise RestApiError(cause=e)