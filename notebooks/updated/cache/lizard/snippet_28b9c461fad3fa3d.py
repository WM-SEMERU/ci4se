def update_dataset(self, dataset_key, **kwargs):
    request = self.__build_dataset_obj(lambda : _swagger.
        DatasetPatchRequest(), lambda name, url, expand_archive,
        description, labels: _swagger.FileCreateOrUpdateRequest(name=name,
        source=_swagger.FileSourceCreateOrUpdateRequest(url=url,
        expand_archive=expand_archive) if url is not None else None,
        description=description, labels=labels), kwargs)
    owner_id, dataset_id = parse_dataset_key(dataset_key)
    try:
        self._datasets_api.patch_dataset(owner_id, dataset_id, request)
    except _swagger.rest.ApiException as e:
        raise RestApiError(cause=e)