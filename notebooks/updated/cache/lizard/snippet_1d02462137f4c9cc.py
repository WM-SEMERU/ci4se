def upload_file(self, dataset_key, name, file_metadata={}, **kwargs):
    owner_id, dataset_id = parse_dataset_key(dataset_key)
    try:
        self._uploads_api.upload_file(owner_id, dataset_id, name, **kwargs)
        if file_metadata:
            self.update_dataset(dataset_key, files=file_metadata)
    except _swagger.rest.ApiException as e:
        raise RestApiError(cause=e)